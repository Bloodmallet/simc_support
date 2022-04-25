"""
Example implementation written for /simc_support/game_data/partial_tree.jpg
"""
import dataclasses
import enum
import json
import pkg_resources
import typing


class MissingInitializationError(Exception):
    pass


@dataclasses.dataclass(unsafe_hash=True)
class Talent:
    full_name: str
    max_rank: int = dataclasses.field(default=1, repr=False)
    # talent_type


@dataclasses.dataclass(unsafe_hash=True)
class TreeNode:
    talent: Talent
    parent_names: typing.Set[str] = dataclasses.field(default_factory=set, repr=False)
    child_names: typing.Set[str] = dataclasses.field(default_factory=set, repr=False)
    # octagon choice nodes
    sibling_names: typing.Set[str] = dataclasses.field(default_factory=set, repr=False)

    parents: typing.List["TreeNode"] = dataclasses.field(
        default_factory=list, init=False, repr=False
    )
    children: typing.List["TreeNode"] = dataclasses.field(
        default_factory=list, init=False, repr=False
    )
    siblings: typing.List["TreeNode"] = dataclasses.field(
        default_factory=list, init=False, repr=False
    )

    def _is_initialized(self) -> bool:
        combined_set = set()
        combined_set.union(self.parents, self.children, self.siblings)
        return any(combined_set)

    # def is_selectable(self) -> bool:
    #     if not self._is_initialized():
    #         raise MissingInitializationError(f"{self} was not initialized yet.")
    #     return any(
    #         [node.invested_points == node.talent.max_rank for node in self.parents]
    #     )


@dataclasses.dataclass
class SelectedTreeNode:
    tree_node: TreeNode
    rank: int


def create_nodes() -> typing.List[TreeNode]:
    """See /simc_support/game_data/partial_tree.jpg

    Returns:
        typing.List[TreeNode]: Representation of /simc_support/game_data/partial_tree.jpg
    """
    nodes: typing.List[TreeNode] = []

    # row 1
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="A1",
            ),
        )
    )
    # row 2
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="B1",
            ),
            parent_names={"A1"},
        )
    )
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="B2",
                max_rank=2,
            ),
            parent_names={"A1"},
        )
    )
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="B3",
            ),
            parent_names={"A1"},
        )
    )
    # row 3
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="C1",
            ),
            parent_names={"B1"},
        )
    )
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="C2",
            ),
            parent_names={"B2"},
        )
    )
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="C3",
            ),
            parent_names={"B3"},
        )
    )
    # row 4
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="D1",
                max_rank=2,
            ),
            parent_names={"C1"},
        )
    )
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="D2",
                max_rank=2,
            ),
            parent_names={"C3"},
        )
    )
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="D3",
                max_rank=2,
            ),
            parent_names={"C3"},
        )
    )
    # row 5
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="E1",
                max_rank=3,
            ),
            parent_names={"C1"},
        )
    )
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="E2",
            ),
            parent_names={"D1", "D2"},
            sibling_names={"E3"},
        )
    )
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="E3",
            ),
            parent_names={"D1", "D2"},
            sibling_names={"E2"},
        )
    )
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="E4",
                max_rank=1,
            ),
            parent_names={"C3"},
        )
    )
    # row 6
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="F1",
                max_rank=1,
            ),
            parent_names={"E1"},
        )
    )
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="F2",
                max_rank=2,
            ),
            parent_names={"E2", "E3"},
        )
    )
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="F3",
                max_rank=2,
            ),
            parent_names={"E2", "E3"},
        )
    )
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="F4",
                max_rank=1,
            ),
            parent_names={"E4"},
        )
    )

    # row 7
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="G1",
                max_rank=1,
            ),
            parent_names={"F1", "F2"},
            sibling_names={"G2"},
        )
    )
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="G2",
                max_rank=1,
            ),
            parent_names={"F1", "F2"},
            sibling_names={"G1"},
        )
    )
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="G3",
                max_rank=1,
            ),
            parent_names={"F3", "F4"},
        )
    )
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="G4",
                max_rank=2,
            ),
            parent_names={"F4"},
        )
    )

    # row 8
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="H1",
                max_rank=1,
            ),
            parent_names={
                "F1",
            },
            sibling_names={"H2"},
        )
    )
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="H2",
                max_rank=1,
            ),
            parent_names={
                "F1",
            },
            sibling_names={"H1"},
        )
    )
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="H3",
                max_rank=1,
            ),
            parent_names={"G1", "G2", "G3"},
        )
    )
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="H4",
                max_rank=1,
            ),
            parent_names={"G4"},
        )
    )

    # row 9
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="I1",
                max_rank=1,
            ),
            parent_names={"H1", "H2"},
        )
    )
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="I2",
                max_rank=1,
            ),
            parent_names={"H1", "H2"},
        )
    )
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="I3",
                max_rank=2,
            ),
            parent_names={"H1", "H2", "H3"},
        )
    )
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="I4",
                max_rank=2,
            ),
            parent_names={"H3", "H4"},
        )
    )
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="I5",
                max_rank=1,
            ),
            parent_names={"H4"},
        )
    )

    # row 10
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="J1",
                max_rank=1,
            ),
            parent_names={"I1"},
            sibling_names={"J2"},
        )
    )
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="J2",
                max_rank=1,
            ),
            parent_names={"I1"},
            sibling_names={"J1"},
        )
    )
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="J3",
                max_rank=1,
            ),
            parent_names={"I3", "I4"},
            sibling_names={"J4"},
        )
    )
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="J4",
                max_rank=1,
            ),
            parent_names={"I3", "I4"},
            sibling_names={"J3"},
        )
    )
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="J5",
                max_rank=1,
            ),
            parent_names={"I5"},
            sibling_names={"J6"},
        )
    )
    nodes.append(
        TreeNode(
            talent=Talent(
                full_name="J6",
                max_rank=1,
            ),
            parent_names={"I5"},
            sibling_names={"J5"},
        )
    )

    return nodes


def initialize(nodes: typing.List[TreeNode]) -> typing.List[TreeNode]:
    t_dict = {n.talent.full_name: n for n in nodes}

    for node in nodes:
        for name in node.parent_names:
            # add parent
            node.parents.append(t_dict[name])

            # add child
            if node not in t_dict[name].children:
                t_dict[name].children.append(node)
        # add siblings
        for name in node.sibling_names:
            node.siblings.append(t_dict[name])

    return nodes


NODES: typing.List[TreeNode] = initialize(create_nodes())


@dataclasses.dataclass
class NodePath:
    selected_nodes: typing.List[SelectedTreeNode] = dataclasses.field(
        default_factory=list
    )

    def __post_init__(self):
        self.selected_nodes = sorted(
            self.selected_nodes, key=lambda n: f"{n.tree_node.talent.full_name}{n.rank}"
        )

    @property
    def invested_points(self) -> int:
        if not hasattr(self, "_invested_points"):
            self._invested_points = sum([n.rank for n in self.selected_nodes])
        return self._invested_points

    def __repr__(self) -> str:
        return ";".join(
            [
                n.tree_node.talent.full_name + ":" + str(n.rank)
                for n in self.selected_nodes
            ]
        )

    def verify(self) -> bool:
        # check if a talent exists twice
        for node in self.selected_nodes:
            if (
                len(
                    [
                        n
                        for n in self.selected_nodes
                        if n.tree_node.talent.full_name
                        == node.tree_node.talent.full_name
                    ]
                )
                != 1
            ):
                return False

        return True


@dataclasses.dataclass
class NodePaths:
    paths: typing.List[NodePath] = dataclasses.field(default_factory=list)

    def append(self, node_path: NodePath) -> None:
        if node_path not in self.paths:
            self.paths.append(node_path)


def grow_paths(nodes: typing.List[TreeNode], points: int) -> typing.List[NodePath]:
    paths: typing.List[NodePath] = []
    invested_points = 0

    starting_points = [n for n in nodes if len(n.parents) == 0]
    for start in starting_points:
        # print(f"adding starting point {start}")
        paths.append(
            NodePath(
                selected_nodes=[
                    SelectedTreeNode(
                        tree_node=start,
                        rank=1,
                    )
                ]
            )
        )
    invested_points += 1

    #   starting node/-s are my starting paths:
    #   for each existing path find all potential children and their potential ranks
    #   create copies of the existing path and add each such child
    #   repeat until no children can be found anywhere
    #
    #   filter by invested points
    #   or abort path generation early based on invested points
    def _grow_paths_by_one(paths: typing.List[NodePath]) -> typing.List[NodePath]:
        """Add new potential paths. Remove used path."""
        print(f"{paths[0].invested_points}: {len(paths)}")

        new_paths = NodePaths()
        for path in paths:
            # add paths with additional nodes
            potential_children: typing.List[TreeNode] = []
            tree_nodes = [n.tree_node for n in path.selected_nodes]
            for node in path.selected_nodes:
                # skip if node is not fully skilled -> we can't have children anyway
                if node.rank != node.tree_node.talent.max_rank:
                    continue

                # create a new path for each child
                for child in node.tree_node.children:
                    sibling_is_already_in_use = any(
                        [s in tree_nodes for s in child.siblings]
                    )
                    if sibling_is_already_in_use:
                        continue

                    if child not in tree_nodes + potential_children:
                        potential_children.append(child)
            # print(f"potential children: {potential_children}")
            for node in potential_children:
                new_nodes = path.selected_nodes + [
                    SelectedTreeNode(tree_node=node, rank=1)
                ]
                new_path = NodePath(selected_nodes=new_nodes)
                new_paths.append(new_path)
            # print("new paths")
            # print(new_paths)

            # add paths with incremented nodes
            potential_increments = [
                node
                for node in path.selected_nodes
                if node.rank < node.tree_node.talent.max_rank
            ]
            # print(f"potential increments: {potential_increments}")
            for potential_increment in potential_increments:
                nodes_without_old = [
                    p for p in path.selected_nodes if p != potential_increment
                ]
                new_nodes = nodes_without_old + [
                    SelectedTreeNode(
                        tree_node=potential_increment.tree_node,
                        rank=potential_increment.rank + 1,
                    )
                ]
                new_path = NodePath(
                    # might need a copy
                    selected_nodes=new_nodes
                )

                new_paths.append(new_path)

        return new_paths.paths

    while paths[0].invested_points != points:
        paths = _grow_paths_by_one(paths=paths)

    print(f"{paths[0].invested_points}: {len(paths)}")
    return paths


def cut_paths(nodes: typing.List[TreeNode], points: int) -> typing.List[NodePath]:
    full_starting_trees: typing.List[typing.List[TreeNode]] = [[]]
    for node in nodes:
        if node.siblings:
            is_already_in_trees = any([node in n for n in full_starting_trees])
            if is_already_in_trees:
                continue
            else:
                new_full_trees = [t + [node] for t in full_starting_trees]
                for sibling in node.siblings:
                    new_full_trees += [t + [sibling] for t in full_starting_trees]

                full_starting_trees = new_full_trees
        else:
            full_starting_trees = [t + [node] for t in full_starting_trees]

    node_paths = NodePaths(
        [
            NodePath([SelectedTreeNode(n, n.talent.max_rank) for n in tree])
            for tree in full_starting_trees
        ]
    )

    # unify_dict = {str(path): path for path in node_paths}
    # node_paths = list(unify_dict.values())

    while sum([p.invested_points for p in node_paths.paths]) > points * len(
        node_paths.paths
    ):
        print(f"{node_paths.paths[0].invested_points}: {len(node_paths.paths)}")
        reduced_paths = NodePaths()
        for path in node_paths.paths:
            active_tree_nodes = [n.tree_node for n in path.selected_nodes]
            reduceable_nodes: typing.List[SelectedTreeNode] = []
            for node in path.selected_nodes:
                # add node as reduceable if it has no children
                child_is_in_use = any(
                    [n in active_tree_nodes for n in node.tree_node.children]
                )
                if not child_is_in_use and node not in reduceable_nodes:
                    reduceable_nodes.append(node)

                # add node as reduceable if all children have other "full" parents
                has_alternative_paths: typing.List[bool] = []
                for child in node.tree_node.children:
                    child_has_multiple_parents = len(child.parents) > 1
                    if not child_has_multiple_parents:
                        has_alternative_paths.append(False)
                        continue

                    other_parents = [p for p in child.parents if p != node.tree_node]
                    other_parent_selected_tree_nodes: typing.List[SelectedTreeNode] = []
                    for parent in other_parents:
                        for n in path.selected_nodes:
                            if n.tree_node == parent:
                                other_parent_selected_tree_nodes.append(n)
                    if any(
                        [
                            n.rank == n.tree_node.talent.max_rank
                            for n in other_parent_selected_tree_nodes
                        ]
                    ):
                        has_alternative_paths.append(True)
                if all(has_alternative_paths):
                    reduceable_nodes.append(node)

            for r_node in reduceable_nodes:
                if r_node.rank == 1:
                    new_path = NodePath([n for n in path.selected_nodes if n != r_node])
                    reduced_paths.append(new_path)
                else:
                    new_path = NodePath(
                        [
                            n
                            if n != r_node
                            else SelectedTreeNode(n.tree_node, n.rank - 1)
                            for n in path.selected_nodes
                        ]
                    )
                    reduced_paths.append(new_path)

        node_paths = reduced_paths

    return node_paths.paths
