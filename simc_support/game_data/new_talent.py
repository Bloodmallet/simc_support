import datetime
import enum
import itertools
import logging
import typing

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
    __slots__ = (
        "name",
        "talent_type",
        "required_invested_points",
        "parent_names",
        "children_names",
        "sibling_names",
        "index",
        "parents",
        "children",
        "siblings",
    )

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
        # return f"{self.name}({self.index})"
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

    def is_selected(self, tree: str) -> bool:
        return tree[self.index] == "1"

    def has_selected_children(self, tree: str) -> bool:
        if not self.children:
            return False
        return any([c.is_selected(tree) for c in self.children])

    def has_selected_parents(self, tree: str) -> bool:
        if not self.parents:
            return False
        return any([p.is_selected(tree) for p in self.parents])

    def has_selected_siblings(self, tree: str) -> bool:
        if not self.siblings:
            return False
        return any([p.is_selected(tree) for p in self.siblings])

    def is_gate_satisfied(self, tree: str) -> bool:
        if self.required_invested_points < 1:
            return True
        return (
            sum([int(selected) for selected in tree]) >= self.required_invested_points
        )

    def select(self, tree: str) -> str:
        """Create a new path tuple."""

        if not self.is_gate_satisfied(tree):
            raise NotEnoughPointsInvestedError(
                f"Node {self.name} at index {self.index} can't be selected at {tree} because not enough points were invested in the current tree."
            )

        new_tree = tree[: self.index] + "1" + tree[self.index + 1 :]
        return new_tree

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
                        name="".join([name, str(rank)]),
                        talent_type=talent_type,
                        required_invested_points=required_invested_points,
                        parent_names=parent_names,
                        children_names=("".join([name, str(rank + 1)]),),
                    )
                )
            elif rank == max_rank:
                talents.append(
                    Talent(
                        name="".join([name, str(rank)]),
                        talent_type=talent_type,
                        required_invested_points=required_invested_points,
                        parent_names=("".join([name, str(rank - 1)]),),
                        children_names=children_names,
                    )
                )
            else:
                talents.append(
                    Talent(
                        name=name + str(rank),
                        talent_type=talent_type,
                        required_invested_points=required_invested_points,
                        parent_names=("".join([name, str(rank - 1)]),),
                        children_names=("".join([name, str(rank + 1)]),),
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
            logger.error(
                f"{t.index}>-1, {len(t.parent_names)}=={len(t.parents)}, {len(t.children_names)}=={len(t.children)}"
            )
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


def remove_choices(talents: typing.Tuple[Talent, ...]) -> typing.Tuple[Talent, ...]:
    """Removes sibling/choice nodes by ensuring only one represents them. New talents are created."""
    single_choiced: typing.List[Talent] = []
    ignored_nodes: typing.List[str] = []
    for t in talents:
        if all([t.name < s for s in t.sibling_names]):
            single_choiced.append(
                Talent(
                    name=t.name,
                    talent_type=t.talent_type,
                    required_invested_points=t.required_invested_points,
                    parent_names=t.parent_names,
                    children_names=t.children_names,
                    sibling_names=t.sibling_names,
                )
            )
        else:
            logger.info(f"Temporarily ignoring {t.name}.")
            ignored_nodes.append(t.name)
    # remove ignored nodes from parent names and children
    for t in single_choiced:
        t.sibling_names = ()
        t.siblings = ()
        t.parents = ()
        t.children = ()
        t.parent_names = tuple((p for p in t.parent_names if p not in ignored_nodes))
        t.children_names = ()

    return _talent_post_init(tuple(single_choiced))


def readd_choices(
    talents: typing.Tuple[Talent, ...],
    single_choice_talents: typing.Tuple[Talent, ...],
    paths: typing.List[str],
) -> typing.Tuple[str, ...]:
    no_choice_to_talents_map: typing.Dict[Talent, Talent] = {}
    for n in single_choice_talents:
        for t in talents:
            if n.name == t.name:
                no_choice_to_talents_map[n] = t

    _original_choices = {
        n: tuple([n] + list(n.siblings)) for n in talents if n.sibling_names
    }

    prepared_choices: typing.Dict[Talent, typing.Tuple[Talent]] = {}
    for n in single_choice_talents:
        for c in _original_choices:
            if n.name == c.name:
                prepared_choices[n] = _original_choices[c]

    trees: typing.List[str] = []
    for path in paths:
        included_choice_nodes = {
            n: v for n, v in prepared_choices.items() if n.is_selected(path)
        }
        blueprint = "".join(["0" for _ in talents])
        for talent in single_choice_talents:
            if talent not in included_choice_nodes and talent.is_selected(path):
                blueprint = (
                    blueprint[: no_choice_to_talents_map[talent].index]
                    + "1"
                    + blueprint[no_choice_to_talents_map[talent].index + 1 :]
                )
        blueprint = blueprint

        choice_combinations = itertools.product(*included_choice_nodes.values())
        for combination in choice_combinations:
            talent: Talent
            local_copy = blueprint
            for talent in combination:
                local_copy = talent.select(local_copy)
            trees.append(local_copy)

    return tuple(trees)


def igrow(talents: typing.Tuple[Talent, ...], points: int) -> typing.Tuple[str, ...]:

    prepared_talents = remove_choices(talents)

    empty_path = "".join(["0" for _ in prepared_talents])

    # key : value
    # path: next growable Talents
    existing_paths: typing.Dict[str, typing.Set[Talent]] = {}
    existing_paths[empty_path] = {t for t in prepared_talents if len(t.parents) == 0}

    for invested_points in range(points + 1):
        start_time = datetime.datetime.utcnow()

        new_paths: typing.Dict[str, typing.Set[Talent]] = {}

        for path, entry_points in existing_paths.items():

            for talent in entry_points:
                new_path: str = ""
                try:
                    new_path = talent.select(path)
                except NotEnoughPointsInvestedError:
                    # this entry point needs to stay relevant for the time enough points are invested
                    pass

                if new_path and new_path not in new_paths:
                    new_entry_points = entry_points.copy()
                    new_entry_points.remove(talent)

                    for child in talent.children:
                        if not child.is_selected(new_path):
                            new_entry_points.add(child)

                    new_paths[new_path] = new_entry_points

        existing_paths = new_paths

        logger.info(
            f"{invested_points}: {len(existing_paths)} ({datetime.datetime.utcnow()-start_time})"
        )

    logger.info("Unpacking choice nodes")
    start_time = datetime.datetime.utcnow()
    trees = readd_choices(talents, prepared_talents, list(existing_paths.keys()))
    logger.info(f"Unpacked: {len(trees)} ({datetime.datetime.utcnow()-start_time})")

    return tuple(trees)
