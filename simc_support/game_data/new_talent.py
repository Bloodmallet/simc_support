import datetime
import enum
import itertools
import json
import logging
import pkg_resources
import typing

logger = logging.getLogger(__name__)

T = typing.TypeVar("T")
ID = typing.Union[int, str]


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
        self.talents: typing.Tuple[Talent, ...] = talents
        self.ranks: typing.Tuple[int, ...] = ranks

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

    @property
    def is_initialized(self) -> bool:
        return all(
            [
                self.index > -1,
                len(self.parent_ids) == len(self.parents),
                len(self.children_ids) == len(self.children),
            ]
        )

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
    __slots__ = ("tree_nodes",)

    def __init__(self, tree_nodes: typing.Tuple[TreeNode, ...]) -> None:
        self.tree_nodes: typing.Tuple[TreeNode, ...] = tree_nodes

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
                        rank=rank,
                        max_rank=max_rank,
                        x=x,
                        y=y,
                        talents=talents,
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
    def grow(
        self, *, points: int, unwanted_nodes: typing.Iterable[TreeNode] = ()
    ) -> typing.List["TreePath"]:

        empty_path = TreePath(tree=self)

        # key : value
        # path: next growable Talents
        existing_paths: typing.Dict[TreePath, typing.Set[TreeNode]] = {}
        # if a starting node requires more points than already invested it'll just idle around
        existing_paths[empty_path] = {
            t
            for t in self.tree_nodes
            if len(t.parents) == 0 and t not in unwanted_nodes
        }

        for invested_points in range(1, points + 1):
            start_time = datetime.datetime.utcnow()

            new_paths: typing.Dict[TreePath, typing.Set[TreeNode]] = {}

            for path, entry_points in existing_paths.items():

                for node in entry_points:
                    try:
                        new_path = path.select(node)
                    except NotEnoughPointsInvestedError:
                        # this entry point needs to stay relevant for the time enough points are invested
                        # logger.info(
                        #     f"Skipping {talent} for now. Not enough points invested yet."
                        # )
                        continue

                    if new_path not in new_paths:
                        new_entry_points = entry_points.copy()

                        if new_path.is_at_max_rank(node):
                            new_entry_points.remove(node)

                            for child in node.children:
                                if (
                                    child not in unwanted_nodes
                                    and not new_path.is_at_max_rank(child)
                                ):
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


class TreePath:
    __slots__ = (
        "path",
        "invested_points",
    )

    def __eq__(self, __o: object) -> bool:
        return self.path == __o.path  # type: ignore

    def __hash__(self) -> int:
        return hash(self.path)

    def __init__(
        self,
        *,
        tree: typing.Optional[Tree] = None,
        path: typing.Optional[typing.Tuple[int, ...]] = None,
        invested_points: typing.Optional[int] = None,
    ) -> None:
        if path is None and invested_points is None and tree is None:
            raise ValueError("All input for TreePath creation was None.")

        if path is None and invested_points is None and tree is not None:
            self.path: typing.Tuple[int, ...] = tuple(0 for _ in tree.tree_nodes)
            self.invested_points = 0

        elif path is not None and invested_points is not None and tree is None:
            self.path = path
            self.invested_points = invested_points
        else:
            raise ValueError("TreePath was created with wrong input combination.")

    def select(self, tree_node: TreeNode, raise_exception: bool = True) -> "TreePath":
        if (
            raise_exception
            and self.invested_points < tree_node.required_invested_points
        ):
            raise NotEnoughPointsInvestedError(
                f"Node {tree_node.name} at index {tree_node.index} can't be selected at {self.path} because not enough points were invested in the current tree ({self.invested_points} < {tree_node.required_invested_points})."
            )

        new_path = (
            *self.path[: tree_node.index],
            self.path[tree_node.index] + 1,
            *self.path[tree_node.index + 1 :],
        )

        return TreePath(path=new_path, invested_points=self.invested_points + 1)

    def is_gate_satisfied(self, tree_node: TreeNode) -> bool:
        if tree_node.required_invested_points < 1:
            return True
        return self.invested_points >= tree_node.required_invested_points

    def is_at_max_rank(self, tree_node: TreeNode) -> bool:
        return self.path[tree_node.index] == tree_node.max_rank

    def has_selected_children(self, tree_node: TreeNode) -> bool:
        if not tree_node.children:
            return False
        return any([self.is_at_max_rank(c) for c in tree_node.children])

    def has_selected_parents(self, tree_node: TreeNode) -> bool:
        if not tree_node.parents:
            return False
        return any([self.is_at_max_rank(p) for p in tree_node.parents])

    def get_rank(self, tree_node: TreeNode) -> int:
        return self.path[tree_node.index]


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
            talents = []
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


class DepthFirstSearch:
    """https://en.wikipedia.org/wiki/Depth-first_search"""

    def __init__(self) -> None:
        self.tree: typing.Tuple[TreeNode, ...] = ()

    def non_recursion(self, G, v):
        """
        procedure DFS_iterative(G, v) is
            let S be a stack
            S.push(v)
            while S is not empty do
                v = S.pop()
                if v is not labeled as discovered then
                    label v as discovered
                    for all edges from v to w in G.adjacentEdges(v) do
                        S.push(w)
        """

        known_v = set()

        # stack, append & pop
        S = []
        S.append(v)

        while S:
            v = S.pop()
            if v in known_v:
                known_v.add(v)
                for child in v:
                    S.append(child)

    def recursive(self, G, v):
        """
        procedure DFS(G, v) is
            label v as discovered
            for all directed edges from v to w that are in G.adjacentEdges(v) do
                if vertex w is not labeled as discovered then
                    recursively call DFS(G, w)
        """
        known_v = set()
        for child in v:
            if child not in known_v:
                self.recursive(G, child)


class IterativeDeepening:
    """https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search"""

    pass


class TopologicalSort:
    __slots__ = ("nodes", "tree")

    def __init__(self, tree: Tree) -> None:
        # generate new tree, consisting og flattened 1-point nodes
        self.nodes: typing.List[TreeNode] = []
        for node in tree.tree_nodes:
            self.nodes += self._create_ranks(node=node)

        self.tree: Tree = Tree(tuple(self.nodes))

    def is_compact_tree(self, tree: Tree) -> bool:
        specifiers_id = set()
        specifiers_name = set()
        specifiers_talent = set()
        for node in tree.tree_nodes:
            if node.id in specifiers_id:
                return False
            else:
                specifiers_id.add(node.id)

            if node.name in specifiers_name:
                return False
            else:
                specifiers_name.add(node.name)

            for talent in node.talents:
                if talent in specifiers_talent:
                    return False
                else:
                    specifiers_talent.add(talent)
        return True

    def _create_ranks(self, *, node: TreeNode) -> typing.List[TreeNode]:
        """Create 1 point nodes based on `node`."""

        tree_nodes: typing.List[TreeNode] = []

        if node.max_rank == 1:
            return [
                TreeNode(
                    id=" ".join([str(node.id), str(node.max_rank)]),
                    name=" ".join([node.name, str(node.max_rank)]),
                    x=node.x,
                    y=node.y,
                    tree_node_type=node.tree_node_type,
                    required_invested_points=node.required_invested_points,
                    max_rank=node.max_rank,
                    rank=node.max_rank,
                    children_ids=tuple(
                        " ".join([str(n), "1"]) for n in node.children_ids
                    ),
                    talents=node.talents,
                )
            ]

        for rank in range(1, node.max_rank + 1):
            if rank == 1:
                tree_nodes.append(
                    TreeNode(
                        id=" ".join([str(node.id), str(rank)]),
                        name=" ".join([node.name, str(rank)]),
                        tree_node_type=node.tree_node_type,
                        required_invested_points=node.required_invested_points,
                        children_ids=(" ".join([str(node.id), str(rank + 1)]),),
                        rank=rank,
                        max_rank=node.max_rank,
                        x=node.x,
                        y=node.y,
                        talents=node.talents,
                    )
                )
            elif rank == node.max_rank:
                tree_nodes.append(
                    TreeNode(
                        id=" ".join([str(node.id), str(rank)]),
                        name=" ".join([node.name, str(rank)]),
                        tree_node_type=node.tree_node_type,
                        required_invested_points=-1,
                        children_ids=tuple(
                            " ".join([str(n), "1"]) for n in node.children_ids
                        ),
                        rank=rank,
                        max_rank=node.max_rank,
                        x=node.x,
                        y=node.y,
                        talents=node.talents,
                    )
                )
            else:
                tree_nodes.append(
                    TreeNode(
                        id=" ".join([str(node.id), str(rank)]),
                        name=" ".join([node.name, str(rank)]),
                        tree_node_type=node.tree_node_type,
                        required_invested_points=-1,
                        children_ids=(" ".join([str(node.id), str(rank + 1)]),),
                        rank=rank,
                        max_rank=node.max_rank,
                        x=node.x,
                        y=node.y,
                        talents=node.talents,
                    )
                )

        return tree_nodes

    def networkx(
        self, invested_points: int
    ) -> typing.Generator[typing.List[TreeNode], None, None]:
        """https://networkx.org/documentation/stable/_modules/networkx/algorithms/dag.html#all_topological_sorts"""
        # if not G.is_directed():
        #     raise ValueError("Topological sort not defined on undirected graphs.")

        def string_representation(nodes: typing.List[TreeNode]) -> str:
            sorted_nodes = sorted(nodes, key=lambda node: node.name)
            name = " ".join([n.name for n in sorted_nodes])
            return name

        # the names of count and D are chosen to match the global variables in [1]
        # number of edges originating in a vertex v
        # count = dict(G.in_degree())
        parent_count: typing.Dict[TreeNode, int] = {}
        for node in self.tree.tree_nodes:
            parent_count[node] = len(node.parent_ids)
        # vertices with indegree 0
        # D = deque([v for v, d in G.in_degree() if d == 0])
        from collections import deque

        known_paths = set()

        next_nodes = deque([n for n, count in parent_count.items() if count == 0])
        # stack of first value chosen at a position k in the topological sort
        bases: typing.List[TreeNode] = []
        current_sort: typing.List[TreeNode] = []

        # TODO: add gate restrictions
        # TODO: add early exit at `invested_points`
        # do-while construct
        while True:
            assert all([parent_count[v] == 0 for v in next_nodes])

            # if len(current_sort) == len(G):
            # if len(current_sort) == len(self.tree.tree_nodes):
            if len(current_sort) == 20:
                name = string_representation(current_sort[:invested_points])
                if name not in known_paths:
                    logger.info(name)
                    known_paths.add(name)
                    yield list(current_sort)
                else:
                    pass
                    # logger.info(f"dublicate {name}")

                # clean-up stack
                while len(current_sort) > 0:
                    assert len(bases) == len(current_sort)
                    q = current_sort.pop()

                    # "restores" all edges (q, x)
                    # NOTE: it is important to iterate over edges instead
                    # of successors, so count is updated correctly in multigraphs
                    # for _, j in G.out_edges(q):
                    for j in q.children:
                        parent_count[j] += 1
                        assert parent_count[j] >= 0
                    # remove entries from D
                    while len(next_nodes) > 0 and parent_count[next_nodes[-1]] > 0:
                        next_nodes.pop()

                    # corresponds to a circular shift of the values in D
                    # if the first value chosen (the base) is in the first
                    # position of D again, we are done and need to consider the
                    # previous condition
                    next_nodes.appendleft(q)
                    if next_nodes[-1] == bases[-1]:
                        # all possible values have been chosen at current position
                        # remove corresponding marker
                        bases.pop()
                    else:
                        # there are still elements that have not been fixed
                        # at the current position in the topological sort
                        # stop removing elements, escape inner loop
                        break

            else:
                if len(next_nodes) == 0:
                    raise ValueError("Graph contains a cycle.")

                # choose next node
                q = next_nodes.pop()
                # "erase" all edges (q, x)
                # NOTE: it is important to iterate over edges instead
                # of successors, so count is updated correctly in multigraphs
                # for _, j in G.out_edges(q):
                for j in q.children:
                    parent_count[j] -= 1
                    assert parent_count[j] >= 0
                    if parent_count[j] == 0:
                        next_nodes.append(j)
                current_sort.append(q)

                # base for current position might _not_ be fixed yet
                if len(bases) < len(current_sort):
                    bases.append(q)

            if len(bases) == 0:
                break


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
