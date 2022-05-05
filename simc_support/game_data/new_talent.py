import datetime
import typing
import logging
import enum

logger = logging.getLogger(__name__)
T = typing.TypeVar("T")


class InitializationError(Exception):
    pass


class MissingSelectedParentError(Exception):
    pass


class AlreadySelectedError(Exception):
    pass


class SiblingAlreadySelectedError(Exception):
    pass


class NotEnoughPointsInvestedError(Exception):
    pass


class TalentType(enum.Enum):
    PASSIVE = enum.auto()
    ABILITY = enum.auto()
    CHOICE = enum.auto()

    def shape(self) -> str:
        mapping = {
            self.PASSIVE: "oval",
            self.ABILITY: "square",
            self.CHOICE: "octagon",
        }
        return mapping[self]


class Talent:
    def __init__(
        self,
        name: str,
        talent_type: TalentType,
        *,
        required_invested_points: int = 0,
        parent_names: typing.Tuple[str, ...] = tuple(),
        children_names: typing.Tuple[str, ...] = tuple(),
        sibling_names: typing.Tuple[str, ...] = tuple(),
    ) -> None:
        self.name: str = name
        self.talent_type: TalentType = talent_type
        self.required_invested_points: int = 0  # required_invested_points
        self.parent_names: typing.Tuple[str, ...] = parent_names
        self.children_names: typing.Tuple[str, ...] = children_names
        self.sibling_names: typing.Tuple[str, ...] = sibling_names

        self.index: int = -1
        self.parents: typing.Tuple["Talent", ...] = tuple()
        self.children: typing.Tuple["Talent", ...] = tuple()
        self.siblings: typing.Tuple["Talent", ...] = tuple()

    def __repr__(self) -> str:
        return f"{self.name}:{self.index}(p:{self.parent_names},c:{self.children_names},s:{self.sibling_names})"

    @property
    def is_initialized(self) -> bool:
        return all(
            [
                self.index > -1,
                len(self.parent_names) == len(self.parents),
                len(self.children_names) == len(self.children),
                len(self.sibling_names) == len(self.siblings),
            ]
        )

    def is_selected(self, tree: typing.Tuple[bool, ...]) -> bool:
        return tree[self.index]

    def has_selected_children(self, tree: typing.Tuple[bool, ...]) -> bool:
        return any([c.is_selected(tree) for c in self.children])

    def has_selected_parents(self, tree: typing.Tuple[bool, ...]) -> bool:
        return any([p.is_selected(tree) for p in self.parents])

    def select(self, tree: typing.Tuple[bool, ...]) -> typing.Tuple[bool, ...]:
        if tree[self.index]:
            raise AlreadySelectedError(
                f"Node {self.name} at index {self.index} can't be selected at {tree} because node was already selected."
            )

        if len(self.parents) > 0 and not any(
            [parent.is_selected(tree) for parent in self.parents]
        ):
            raise MissingSelectedParentError(
                f"Node {self.name} at index {self.index} can't be selected at {tree} because no parent was selected."
            )

        if len(self.siblings) > 0 and any(
            [sibling.is_selected(tree) for sibling in self.siblings]
        ):
            raise SiblingAlreadySelectedError(
                f"Node {self.name} at index {self.index} can't be selected at {tree} because one of its siblings was already selected."
            )

        if self.required_invested_points > 0 and (
            sum([1 if selected else 0 for selected in tree])
            < self.required_invested_points
        ):
            raise NotEnoughPointsInvestedError(
                f"Node {self.name} at index {self.index} can't be selected at {tree} because not enough points were invested in the current tree."
            )

        new_tree = list(tree).copy()
        new_tree[self.index] = True

        return tuple(new_tree)

    @staticmethod
    def create_ranks(
        name: str,
        talent_type: TalentType,
        max_rank: int,
        *,
        required_invested_points: int = 0,
        parent_names: typing.Tuple[str, ...] = tuple(),
        children_names: typing.Tuple[str, ...] = tuple(),
        # sibling_names: typing.Tuple[str, ...] = tuple(),
    ) -> typing.Tuple["Talent", ...]:
        talents: typing.List[Talent] = []

        for rank in range(1, max_rank + 1):
            if rank == 1:
                talents.append(
                    Talent(
                        name=name + str(rank),
                        talent_type=talent_type,
                        required_invested_points=required_invested_points,
                        parent_names=parent_names,
                        children_names=(name + str(rank + 1),),
                    )
                )
            elif rank == max_rank:
                talents.append(
                    Talent(
                        name=name + str(rank),
                        talent_type=talent_type,
                        required_invested_points=required_invested_points,
                        parent_names=(name + str(rank - 1),),
                        children_names=children_names,
                    )
                )
            else:
                talents.append(
                    Talent(
                        name=name + str(rank),
                        talent_type=talent_type,
                        required_invested_points=required_invested_points,
                        parent_names=(name + str(rank - 1),),
                        children_names=(name + str(rank + 1),),
                    )
                )

        return tuple(talents)

    def get_dict(
        self,
    ) -> typing.Dict[str, typing.Union[str, int, typing.Tuple[str, ...]]]:
        return {
            "name": self.name,
            "index": self.index,
            "talent_type": self.talent_type.value,
            "max_rank": 1,
            "required_invested_points": self.required_invested_points,
            "parent_names": self.parent_names,
            "children_names": self.children_names,
            "sibling_names": self.sibling_names,
        }


def _talent_post_init(talents: typing.Tuple[Talent, ...]) -> typing.Tuple[Talent, ...]:
    t_dict = {t.name: t for t in talents}
    # print(t_dict)

    for index, talent in enumerate(talents):
        for name in talent.parent_names:
            parent_names = [n for n in t_dict.keys() if name in n]
            last_parent_name = sorted(parent_names)[-1]

            # add parent
            talent.parents = tuple(list(talent.parents) + [t_dict[last_parent_name]])

            # add child
            if talent.name not in t_dict[last_parent_name].children_names:
                t_dict[last_parent_name].children_names = tuple(
                    list(t_dict[last_parent_name].children_names) + [talent.name]
                )
            if talent not in t_dict[last_parent_name].children:
                t_dict[last_parent_name].children = tuple(
                    list(t_dict[last_parent_name].children) + [talent]
                )

        # add siblings
        for name in talent.sibling_names:
            talent.siblings = tuple(list(talent.siblings) + [t_dict[name]])

        talent.index = index

    for t in talents:
        if not t.is_initialized:
            raise InitializationError(t)

    return talents


def _create_talents() -> typing.Tuple[Talent, ...]:
    """See /simc_support/game_data/partial_tree.jpg

    Returns:
        typing.List[TreeNode]: Representation of /simc_support/game_data/partial_tree.jpg
    """

    class HelperTalents:
        def __init__(self) -> None:
            self.talents: typing.List[Talent] = []

        def append(self, talent: typing.Union[Talent, typing.Iterable[Talent]]) -> None:
            if isinstance(talent, Talent):
                self.talents.append(talent)
            elif isinstance(talent, typing.Iterable):
                for t in talent:
                    self.talents.append(t)
            else:
                pass

    talents = HelperTalents()

    # row 1
    talents.append(
        Talent(
            name="A1",
            talent_type=TalentType.ABILITY,
        )
    )
    # row 2
    talents.append(
        Talent(
            name="B1",
            talent_type=TalentType.ABILITY,
            parent_names=("A1",),
        ),
    )
    talents.append(
        Talent.create_ranks(
            name="B2",
            talent_type=TalentType.PASSIVE,
            max_rank=2,
            parent_names=("A1",),
        ),
    )
    talents.append(
        Talent(
            name="B3",
            talent_type=TalentType.PASSIVE,
            parent_names=("A1",),
        )
    )
    # row 3
    talents.append(
        Talent(
            name="C1",
            talent_type=TalentType.ABILITY,
            parent_names=("B1",),
        )
    )
    talents.append(
        Talent(
            name="C2",
            talent_type=TalentType.ABILITY,
            parent_names=("B2",),
        )
    )
    talents.append(
        Talent(
            name="C3",
            talent_type=TalentType.ABILITY,
            parent_names=("B3",),
        )
    )
    # row 4
    talents.append(
        Talent.create_ranks(
            name="D1",
            talent_type=TalentType.PASSIVE,
            max_rank=2,
            parent_names=("C1",),
        )
    )
    talents.append(
        Talent.create_ranks(
            name="D2",
            talent_type=TalentType.PASSIVE,
            max_rank=2,
            parent_names=("C3",),
        )
    )
    talents.append(
        Talent.create_ranks(
            name="D3",
            talent_type=TalentType.PASSIVE,
            max_rank=2,
            parent_names=("C3",),
        )
    )
    # row 5
    talents.append(
        Talent.create_ranks(
            name="E1",
            talent_type=TalentType.PASSIVE,
            required_invested_points=6,
            max_rank=3,
            parent_names=("C1",),
        )
    )
    talents.append(
        Talent(
            name="E2",
            talent_type=TalentType.CHOICE,
            required_invested_points=6,
            parent_names=(
                "D1",
                "D2",
            ),
            sibling_names=("E3",),
        )
    )
    talents.append(
        Talent(
            name="E3",
            talent_type=TalentType.CHOICE,
            required_invested_points=6,
            parent_names=(
                "D1",
                "D2",
            ),
            sibling_names=("E2",),
        )
    )
    talents.append(
        Talent(
            name="E4",
            talent_type=TalentType.PASSIVE,
            required_invested_points=6,
            parent_names=("C3",),
        )
    )
    # row 6
    talents.append(
        Talent(
            name="F1",
            talent_type=TalentType.PASSIVE,
            parent_names=("E1",),
        )
    )
    talents.append(
        Talent.create_ranks(
            name="F2",
            talent_type=TalentType.PASSIVE,
            max_rank=2,
            parent_names=(
                "E2",
                "E3",
            ),
        )
    )
    talents.append(
        Talent.create_ranks(
            name="F3",
            talent_type=TalentType.PASSIVE,
            max_rank=2,
            parent_names=(
                "E2",
                "E3",
            ),
        )
    )
    talents.append(
        Talent(
            name="F4",
            talent_type=TalentType.PASSIVE,
            parent_names=("E4",),
        )
    )

    # row 7
    talents.append(
        Talent(
            name="G1",
            talent_type=TalentType.CHOICE,
            parent_names=(
                "F1",
                "F2",
            ),
            sibling_names=("G2",),
        )
    )
    talents.append(
        Talent(
            name="G2",
            talent_type=TalentType.CHOICE,
            parent_names=(
                "F1",
                "F2",
            ),
            sibling_names=("G1",),
        )
    )
    talents.append(
        Talent(
            name="G3",
            talent_type=TalentType.PASSIVE,
            parent_names=(
                "F3",
                "F4",
            ),
        )
    )
    talents.append(
        Talent.create_ranks(
            name="G4",
            talent_type=TalentType.PASSIVE,
            max_rank=2,
            parent_names=("F4",),
        )
    )

    # row 8
    talents.append(
        Talent(
            name="H1",
            talent_type=TalentType.CHOICE,
            required_invested_points=12,
            parent_names=("F1",),
            sibling_names=("H2",),
        )
    )
    talents.append(
        Talent(
            name="H2",
            talent_type=TalentType.CHOICE,
            required_invested_points=12,
            parent_names=("F1",),
            sibling_names=("H1",),
        )
    )
    talents.append(
        Talent(
            name="H3",
            talent_type=TalentType.PASSIVE,
            required_invested_points=12,
            parent_names=(
                "G1",
                "G2",
                "G3",
            ),
        )
    )
    talents.append(
        Talent(
            name="H4",
            talent_type=TalentType.ABILITY,
            required_invested_points=12,
            parent_names=("G4",),
        )
    )

    # row 9
    talents.append(
        Talent(
            name="I1",
            talent_type=TalentType.PASSIVE,
            parent_names=(
                "H1",
                "H2",
            ),
        )
    )
    talents.append(
        Talent(
            name="I2",
            talent_type=TalentType.PASSIVE,
            parent_names=(
                "H1",
                "H2",
            ),
        )
    )
    talents.append(
        Talent.create_ranks(
            name="I3",
            talent_type=TalentType.PASSIVE,
            max_rank=2,
            parent_names=(
                "H1",
                "H2",
                "H3",
            ),
        )
    )
    talents.append(
        Talent.create_ranks(
            name="I4",
            talent_type=TalentType.PASSIVE,
            max_rank=2,
            parent_names=(
                "H3",
                "H4",
            ),
        )
    )
    talents.append(
        Talent(
            name="I5",
            talent_type=TalentType.PASSIVE,
            parent_names=("H4",),
        )
    )

    # row 10
    talents.append(
        Talent(
            name="J1",
            talent_type=TalentType.CHOICE,
            parent_names=("I1",),
            sibling_names=("J2",),
        )
    )
    talents.append(
        Talent(
            name="J2",
            talent_type=TalentType.CHOICE,
            parent_names=("I1",),
            sibling_names=("J1",),
        )
    )
    talents.append(
        Talent(
            name="J3",
            talent_type=TalentType.CHOICE,
            parent_names=(
                "I3",
                "I4",
            ),
            sibling_names=("J4",),
        )
    )
    talents.append(
        Talent(
            name="J4",
            talent_type=TalentType.CHOICE,
            parent_names=(
                "I3",
                "I4",
            ),
            sibling_names=("J3",),
        )
    )
    talents.append(
        Talent(
            name="J5",
            talent_type=TalentType.CHOICE,
            parent_names=("I5",),
            sibling_names=("J6",),
        )
    )
    talents.append(
        Talent(
            name="J6",
            talent_type=TalentType.CHOICE,
            parent_names=("I5",),
            sibling_names=("J5",),
        )
    )

    return tuple(talents.talents)


TALENTS: typing.Tuple[Talent, ...] = _talent_post_init(_create_talents())


def grow(
    talents: typing.Tuple[Talent, ...], points: int
) -> typing.Tuple[typing.Tuple[bool, ...], ...]:

    invested_points: int = 0
    existing_paths: typing.Set[typing.Tuple[bool, ...]] = set()
    empty_path = [False for _ in talents]
    existing_paths.add(tuple(empty_path))

    while invested_points < points:
        start_time = datetime.datetime.utcnow()

        new_paths: typing.Set[typing.Tuple[bool, ...]] = set()
        for path in existing_paths:
            # it's probably cleverer to traverse through the actual child elements,
            # that would terminate early instead of checking all talents every time
            for talent in talents:
                try:
                    new_path = talent.select(path)
                except AlreadySelectedError:
                    pass
                except MissingSelectedParentError:
                    pass
                except SiblingAlreadySelectedError:
                    pass
                except NotEnoughPointsInvestedError:
                    pass
                else:
                    new_paths.add(new_path)

        existing_paths = new_paths
        invested_points += 1

        logger.info(
            f"{invested_points}: {len(existing_paths)} ({datetime.datetime.utcnow()-start_time})"
        )
    return tuple(existing_paths)


def igrow(
    talents: typing.Tuple[Talent, ...], points: int
) -> typing.Tuple[typing.Tuple[bool, ...], ...]:

    invested_points: int = 0
    existing_paths: typing.Dict[typing.Tuple[bool, ...], typing.Set[Talent]] = {}
    empty_path = [False for _ in talents]
    existing_paths[tuple(empty_path)] = {t for t in talents if len(t.parents) == 0}

    while invested_points < points:
        start_time = datetime.datetime.utcnow()

        new_paths: typing.Dict[typing.Tuple[bool, ...], typing.Set[Talent]] = {}

        for path, entry_points in existing_paths.items():

            # it's probably cleverer to traverse through the actual child elements,
            # that would terminate early instead of checking all talents every time
            for talent in entry_points:
                new_entry_points = entry_points.copy()
                try:
                    new_path = talent.select(path)
                except AlreadySelectedError:
                    # new_entry_points.remove(talent)
                    pass
                except SiblingAlreadySelectedError:
                    # new_entry_points.remove(talent)
                    pass
                except NotEnoughPointsInvestedError:
                    # this entry points needs to stay relevant for the time enough points are invested
                    pass
                else:
                    for child in talent.children:
                        new_entry_points.add(child)

                    new_entry_points.remove(talent)
                    new_paths[new_path] = new_entry_points

        existing_paths = new_paths
        invested_points += 1

        logger.info(
            f"{invested_points}: {len(existing_paths)} ({datetime.datetime.utcnow()-start_time})"
        )
    return tuple(existing_paths)
