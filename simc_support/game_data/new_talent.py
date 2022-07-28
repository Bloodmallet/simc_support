import datetime
import enum
import itertools
import json
import logging
import pkg_resources
import typing

logger = logging.getLogger(__name__)

T = typing.TypeVar("T")
ID = int


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


class LeafsDependOnNode(Exception):
    pass


class TalentType(enum.Enum):
    ACTIVE = "active"
    PASSIVE = "passive"

    def shape(self) -> str:
        mapping = {
            TalentType.PASSIVE: "oval",
            TalentType.ACTIVE: "square",
        }
        return mapping[self]


class Talent:
    """A Talent is the passive or active ability itself. Per click you're only interacting with one talent."""

    __slots__ = ("id", "max_ranks", "type", "name", "spell_id", "icon")

    def __init__(
        self,
        *,
        id: int,
        max_ranks: int,
        type: TalentType,
        name: str,
        spell_id: int,
        icon: str,
    ) -> None:
        self.id: int = id
        self.max_ranks: int = max_ranks
        self.type: TalentType = type
        self.name: str = name
        self.spell_id: int = spell_id
        self.icon: str = icon


class TalentTree:
    """An actually selected talent tree"""

    def __init__(
        self, talents: typing.Tuple[Talent, ...], ranks: typing.Tuple[int, ...]
    ) -> None:
        self.talents: typing.Tuple[Talent] = talents
        self.ranks: typing.Tuple[int] = ranks

    def rank_talents(self) -> typing.Iterable[typing.Tuple[int, Talent]]:
        return zip(self.ranks, self.talents)


class TreeNodeType(enum.Enum):
    SINGLE = "single"
    CHOICE = "choice"
    TIERED = "tiered"

    def shape(self) -> str:
        mapping = {
            TreeNodeType.CHOICE: "octagon",
        }
        return mapping[self]


class TreeNode:
    """A TreeNode is one single interactive area in the Tree. A TreeNode can have one to many Talents selectable by it.

    Raises:
        NotEnoughPointsInvestedError: _description_
        LeafsDependOnNode: _description_

    Returns:
        _type_: _description_
    """

    __slots__ = (
        "id",
        "name",
        "tree_node_type",
        "required_invested_points",
        "rank",
        "max_rank",
        "parent_ids",
        "children_ids",
        "index",
        "x",
        "y",
        "parents",
        "children",
        "talents",
    )

    def __init__(
        self,
        *,
        id: ID,
        name: str,
        x: int,
        y: int,
        tree_node_type: TreeNodeType,
        required_invested_points: int = 0,
        max_rank: int = 1,
        rank: int = 0,
        parent_ids: typing.Tuple[ID, ...] = tuple(),
        children_ids: typing.Tuple[ID, ...] = tuple(),
        talents: typing.Tuple[Talent, ...],
    ) -> None:
        self.id: ID = id
        self.name: str = name
        self.x: int = x
        self.y: int = y
        self.tree_node_type: TreeNodeType = tree_node_type
        self.required_invested_points: int = required_invested_points
        # rank of a talent (a talent list of trees has "flattened" talents, only representing exactly one rank)
        self.max_rank: int = max_rank
        self.rank: int = rank
        self.parent_ids: typing.Tuple[ID, ...] = parent_ids
        self.children_ids: typing.Tuple[ID, ...] = children_ids
        self.talents: typing.Tuple[Talent, ...] = talents

        # index within a talent list of a tree
        self.index: int = -1
        self.parents: typing.Tuple["TreeNode", ...] = tuple()
        self.children: typing.Tuple["TreeNode", ...] = tuple()

    def __repr__(self) -> str:
        # return f"{self.name}({self.index})"
        return f"{self.name}:{self.index}(id:{self.id},p:{self.parent_ids},c:{self.children_ids})"

    def get_rank(self, tree: str) -> int:
        return int(tree[self.index])

    @property
    def is_initialized(self) -> bool:
        return all(
            [
                self.index > -1,
                len(self.parent_ids) == len(self.parents),
                len(self.children_ids) == len(self.children),
            ]
        )

    def is_at_max_rank(self, tree: str) -> bool:
        return tree[self.index] == str(self.max_rank)

    def has_selected_children(self, tree: str) -> bool:
        if not self.children:
            return False
        return any([c.is_at_max_rank(tree) for c in self.children])

    def has_selected_parents(self, tree: str) -> bool:
        if not self.parents:
            return False
        return any([p.is_at_max_rank(tree) for p in self.parents])

    def is_gate_satisfied(self, tree: str) -> bool:
        if self.required_invested_points < 1:
            return True
        return (
            sum([int(selected) for selected in tree]) >= self.required_invested_points
        )

    def select(self, tree: str, *, raise_exception: bool = True) -> str:
        """Create a new path tuple."""

        if raise_exception and not self.is_gate_satisfied(tree):
            invested_points = sum([int(selected) for selected in tree])
            raise NotEnoughPointsInvestedError(
                f"Node {self.name} at index {self.index} can't be selected at {tree} because not enough points were invested in the current tree ({invested_points} != {self.required_invested_points})."
            )

        new_tree = (
            tree[: self.index] + str(int(tree[self.index]) + 1) + tree[self.index + 1 :]
        )

        return new_tree

    def get_dict(
        self,
    ) -> typing.Dict[str, typing.Union[ID, str, int, typing.Tuple[ID, ...]]]:

        return {
            "id": self.id,
            "name": self.name,
            "index": self.index,
            "talent_type": str(self.tree_node_type.value),
            "max_rank": 1,
            "required_invested_points": self.required_invested_points,
            "parent_names": self.parent_ids,
            "children_names": self.children_ids,
        }


class Tree:
    __slots__ = (
        "tree_nodes",
        "paths",
    )

    def __init__(self, tree_nodes: typing.Tuple[TreeNode, ...]) -> None:
        self.tree_nodes: typing.Tuple[TreeNode, ...] = tree_nodes
        self.paths: typing.List[str] = []

        self._tree_nodes_post_init()

    @staticmethod
    def create_ranks(
        *,
        id: int,
        name: str,
        tree_node_type: TreeNodeType,
        x: int,
        y: int,
        max_rank: int,
        required_invested_points: int = 0,
        children_ids: typing.Tuple[ID, ...] = tuple(),
        talents: typing.Tuple[Talent, ...] = tuple(),
    ) -> typing.Tuple[TreeNode, ...]:
        """Try to not use this...instead try to work with paths that have multi-ranks"""

        tree_nodes: typing.List[TreeNode] = []

        for rank in range(max_rank, 0, -1):
            if rank == 1:
                tree_nodes.append(
                    TreeNode(
                        id=id,
                        name=name,
                        tree_node_type=tree_node_type,
                        required_invested_points=required_invested_points,
                        children_ids=children_ids,
                        rank=rank,
                        max_rank=max_rank,
                        x=x,
                        y=y,
                        talents=talents,
                    )
                )
            elif rank == max_rank:
                tree_nodes.append(
                    TreeNode(
                        id=id,
                        name=name,
                        tree_node_type=tree_node_type,
                        required_invested_points=-1,
                        children_ids=children_ids,
                        rank=rank,
                        max_rank=max_rank,
                        x=x,
                        y=y,
                        talents=talents,
                    )
                )
            else:
                tree_nodes.append(
                    TreeNode(
                        id=id,
                        name=name,
                        tree_node_type=tree_node_type,
                        required_invested_points=-1,
                        children_ids=children_ids,
                        max_rank=max_rank,
                        x=x,
                        y=y,
                        talents=talents,
                        rank=rank,
                    )
                )

        return tuple(tree_nodes)

    def _tree_nodes_post_init(self) -> None:

        n_dict = {n.id: n for n in self.tree_nodes}

        # set children, parent_ids and parents
        for index, node in enumerate(self.tree_nodes):
            node.index = index

            # children
            node.children = tuple((n_dict[id] for id in node.children_ids))

            for node_id in node.children_ids:
                # parent_ids
                if node.id not in n_dict[node_id].parent_ids:
                    n_dict[node_id].parent_ids = tuple(
                        list(n_dict[node_id].parent_ids) + [node.id]
                    )
                # parents
                if node not in n_dict[node_id].parents:
                    n_dict[node_id].parents = tuple(
                        list(n_dict[node_id].parents) + [node]
                    )

        # ensure everything is working
        for t in self.tree_nodes:
            if not t.is_initialized:
                logger.error(
                    f"{t.index}>-1, {len(t.parent_ids)}=={len(t.parents)}, {len(t.children_ids)}=={len(t.children)}"
                )
                raise InitializationError(t)

    # def grow(self, *, points: int) -> typing.Iterable[TalentTree]:
    def grow(self, *, points: int) -> typing.List[str]:

        empty_path = "".join(["0" for _ in self.tree_nodes])

        # key : value
        # path: next growable Talents
        existing_paths: typing.Dict[str, typing.Set[TreeNode]] = {}
        existing_paths[empty_path] = {
            t
            for t in self.tree_nodes
            if len(t.parents) == 0 and t.required_invested_points == 0
        }

        for invested_points in range(1, points + 1):
            start_time = datetime.datetime.utcnow()

            new_paths: typing.Dict[str, typing.Set[TreeNode]] = {}

            for path, entry_points in existing_paths.items():

                for node in entry_points:
                    new_path: str = ""
                    try:
                        new_path = node.select(path)
                    except NotEnoughPointsInvestedError:
                        # this entry point needs to stay relevant for the time enough points are invested
                        # logger.info(
                        #     f"Skipping {talent} for now. Not enough points invested yet."
                        # )
                        continue

                    if new_path not in new_paths:
                        new_entry_points = entry_points.copy()

                        if node.is_at_max_rank(new_path):
                            new_entry_points.remove(node)

                            for child in node.children:
                                if not child.is_at_max_rank(new_path):
                                    new_entry_points.add(child)

                        new_paths[new_path] = new_entry_points

            existing_paths = new_paths

            logger.info(
                f"{invested_points}: {len(existing_paths)} ({datetime.datetime.utcnow()-start_time})"
            )

        start_time = datetime.datetime.utcnow()
        logger.warning(
            "Choice nodes aren't unpacked. you're not dealing with the actual sum of paths yet."
        )

        return list(existing_paths.keys())

        # # build actual Talent trees, not NodeTrees. Essentially: unpack choice nodes based on what was selected.
        # choice_nodes = {
        #     n.index: n
        #     for n in self.tree_nodes
        #     if n.tree_node_type == TreeNodeType.CHOICE
        # }
        # # 11101110101
        # for path in existing_paths:
        #     selected_choice_talents = [
        #         choice_nodes[i].talents for i in choice_nodes if path[i] != "0"
        #     ]
        #     talent_indizes: typing.Dict[Talent, int] = {
        #         talent: i for i in choice_nodes for talent in choice_nodes[i].talents
        #     }

        #     for choice_talent_combination in itertools.product(
        #         *selected_choice_talents
        #     ):
        #         selected_indexes = {
        #             talent_indizes[t]: t for t in choice_talent_combination
        #         }

        #         talents: typing.List[Talent] = []
        #         ranks: typing.List[int] = []
        #         for index, rank in enumerate(path):
        #             if rank == "0":
        #                 continue

        #             talents.append(
        #                 selected_indexes.get(index, self.tree_nodes[index].talents[0])
        #             )
        #             ranks.append(int(rank))

        #         yield TalentTree(talents=tuple(talents), ranks=tuple(ranks))


def _load_talent_files() -> typing.Dict[str, typing.Any]:
    talents_per_spec = {}

    path = "/".join(("data_files", "trees"))
    for file in pkg_resources.resource_listdir(__name__, path):
        if "raidbots" in file:
            continue

        spec = file.split(".")[0]
        file_path = "/".join((path, file))

        with pkg_resources.resource_stream(__name__, file_path) as f:
            talents_per_spec[spec] = json.load(f)

    return talents_per_spec


def _load_talents(
    loaded_talents: typing.Dict[str, typing.Any]
) -> typing.Dict[str, typing.Tuple[Tree, Tree]]:
    trees: typing.Dict[str, typing.Tuple[Tree, Tree]] = {}

    for spec in loaded_talents.keys():
        # class_tree
        class_nodes: typing.List[TreeNode] = []
        for raw_node in loaded_talents[spec]["classNodes"]:
            talents: typing.List[Talent] = []
            for raw_talent in raw_node["entries"]:
                try:
                    talents.append(
                        Talent(
                            id=raw_talent["id"],
                            max_ranks=raw_talent["maxRanks"],
                            type=TalentType(raw_talent["type"]),
                            name=raw_talent.get("name", "PH"),
                            spell_id=raw_talent.get("spellId", -1),
                            icon=raw_talent["icon"],
                        )
                    )
                except KeyError as e:
                    logger.exception(raw_talent)
                    raise e
            try:
                class_nodes.append(
                    TreeNode(
                        id=raw_node["id"],
                        name=raw_node["name"],
                        x=raw_node["posX"],
                        y=raw_node["posY"],
                        tree_node_type=TreeNodeType(raw_node["type"] or "passive"),
                        required_invested_points=raw_node.get("reqPoints", 0),
                        max_rank=raw_node["maxRanks"],
                        children_ids=tuple(raw_node["next"]),
                        talents=tuple(talents),
                    )
                )
            except ValueError as e:
                logger.exception(raw_node)
                raise e

        # spec tree
        spec_nodes: typing.List[TreeNode] = []
        for raw_node in loaded_talents[spec]["specNodes"]:
            talents: typing.List[Talent] = []
            for raw_talent in raw_node["entries"]:
                try:
                    talents.append(
                        Talent(
                            id=raw_talent["id"],
                            max_ranks=raw_talent["maxRanks"],
                            type=TalentType(raw_talent["type"] or "passive"),
                            name=raw_talent.get("name", "PH"),
                            spell_id=raw_talent.get("spellId", -1),
                            icon=raw_talent["icon"],
                        )
                    )
                except KeyError as e:
                    logger.exception(raw_talent)
                    raise e
            spec_nodes.append(
                TreeNode(
                    id=raw_node["id"],
                    name=raw_node["name"],
                    x=raw_node["posX"],
                    y=raw_node["posY"],
                    tree_node_type=TreeNodeType(raw_node["type"]),
                    required_invested_points=raw_node.get("reqPoints", 0),
                    max_rank=raw_node["maxRanks"],
                    children_ids=tuple(raw_node["next"]),
                    talents=tuple(talents),
                )
            )

        class_tree = Tree(tree_nodes=tuple(class_nodes))
        spec_tree = Tree(tree_nodes=tuple(spec_nodes))

        trees[spec] = (class_tree, spec_tree)

    return trees


TALENTS: typing.Dict[str, typing.Tuple[Tree, Tree]] = _load_talents(
    _load_talent_files()
)


# def readd_choices(
#     talents: typing.Tuple[TreeNode, ...],
#     single_choice_talents: typing.Tuple[TreeNode, ...],
#     paths: typing.List[str],
# ) -> typing.Tuple[str, ...]:
#     """unpack all selected choice talent options

#     Args:
#         talents (typing.Tuple[Talent, ...]): all talents
#         single_choice_talents (typing.Tuple[Talent, ...]): talents with only the first of all choice talents
#         paths (typing.List[str]): selected paths of only the first choice talents

#     Returns:
#         typing.Tuple[str, ...]: unpacked full path using all talents
#     """
#     # dictionary of single_choices that map to their respective original counterpart
#     no_choice_to_talents_map: typing.Dict[TreeNode, TreeNode] = {}
#     for n in single_choice_talents:
#         for t in talents:
#             if n.name == t.name:
#                 no_choice_to_talents_map[n] = t

#     # dictionary of original choice nodes and all their siblings and themselves
#     _original_choices = {
#         n: tuple([n] + list(n.siblings)) for n in talents if n.sibling_ids
#     }

#     # dictionary maps single_choice choice talents to all available original sibling choice talents
#     prepared_choices: typing.Dict[TreeNode, typing.Tuple[TreeNode, ...]] = {}
#     for n in single_choice_talents:
#         for c in _original_choices:
#             if n.name == c.name:
#                 prepared_choices[n] = _original_choices[c]

#     blueprint_all_false = "".join(["0" for _ in talents])

#     trees: typing.List[str] = []
#     for path in paths:
#         included_choice_nodes = {
#             n: v for n, v in prepared_choices.items() if n.is_at_max_rank(path)
#         }

#         # create a blueprint that doesn't have any choice nodes selected
#         blueprint = blueprint_all_false
#         for talent in single_choice_talents:
#             # set talent to matching state if it's not a choice node
#             if talent not in included_choice_nodes and talent.is_at_max_rank(path):
#                 blueprint = no_choice_to_talents_map[talent].select(
#                     blueprint, raise_exception=False
#                 )

#         # create trees for each included choice node combination
#         choice_combinations = itertools.product(*included_choice_nodes.values())
#         for combination in choice_combinations:
#             local_copy = blueprint
#             for talent in combination:
#                 local_copy = talent.select(local_copy)
#             trees.append(local_copy)

#     return tuple(trees)
