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
            parent_names={"C2"},
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
    # nodes.append(
    #     TreeNode(
    #         talent=Talent(
    #             full_name="F1",
    #             max_rank=1,
    #         ),
    #         parent_names={"E1"},
    #     )
    # )
    # nodes.append(
    #     TreeNode(
    #         talent=Talent(
    #             full_name="F2",
    #             max_rank=2,
    #         ),
    #         parent_names={"E2"},
    #     )
    # )
    # nodes.append(
    #     TreeNode(
    #         talent=Talent(
    #             full_name="F3",
    #             max_rank=2,
    #         ),
    #         parent_names={"E3"},
    #     )
    # )
    # nodes.append(
    #     TreeNode(
    #         talent=Talent(
    #             full_name="F4",
    #             max_rank=1,
    #         ),
    #         parent_names={"E4"},
    #     )
    # )

    # row 7
    # nodes.append(
    #     TreeNode(
    #         talent=Talent(
    #             full_name="G1",
    #             max_rank=1,
    #         ),
    #         parent_names={"F1", "F2"},
    #         sibling_names={"G2"},
    #     )
    # )
    # nodes.append(
    #     TreeNode(
    #         talent=Talent(
    #             full_name="G2",
    #             max_rank=1,
    #         ),
    #         parent_names={"F1", "F2"},
    #         sibling_names={"G1"},
    #     )
    # )
    # nodes.append(
    #     TreeNode(
    #         talent=Talent(
    #             full_name="G3",
    #             max_rank=1,
    #         ),
    #         parent_names={"F3", "F4"},
    #     )
    # )
    # nodes.append(
    #     TreeNode(
    #         talent=Talent(
    #             full_name="G4",
    #             max_rank=2,
    #         ),
    #         parent_names={"F3", "F4"},
    #     )
    # )

    # row 8

    # row 9

    # row 10

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

    @property
    def invested_points(self) -> int:
        return sum([n.rank for n in self.selected_nodes])

    def __repr__(self) -> str:
        return " - ".join(
            [
                n.tree_node.talent.full_name + " " + str(n.rank)
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


def create_paths(nodes: typing.List[TreeNode], points: int) -> typing.List[NodePath]:
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
    def _create_paths(paths: typing.List[NodePath]) -> typing.List[NodePath]:
        """Add new potential paths. Remove used path."""
        new_paths: typing.List[NodePath] = []
        for path in paths:
            # add paths with additional nodes
            potential_children: typing.List[TreeNode] = []
            tree_nodes = [n.tree_node for n in path.selected_nodes]
            for node in path.selected_nodes:
                # skip if node is not fully skilled -> we can't have children anyway
                if node.rank != node.tree_node.talent.max_rank:
                    continue

                for child in node.tree_node.children:
                    sibling_is_already_in_use = any(
                        [
                            s
                            for s in child.siblings
                            if s in [n.tree_node for n in path.selected_nodes]
                        ]
                    )
                    if sibling_is_already_in_use:
                        continue

                    if child not in tree_nodes and child not in potential_children:
                        potential_children.append(child)

            # print(f"potential children: {potential_children}")
            for node in potential_children:
                new_paths.append(
                    NodePath(
                        # might need a copy
                        selected_nodes=path.selected_nodes
                        + [SelectedTreeNode(tree_node=node, rank=1)]
                    )
                )
            # print("new paths")
            # print(new_paths)

            # add paths with incremented nodes
            potential_increments: typing.List[
                typing.Tuple[SelectedTreeNode, TreeNode]
            ] = []
            for node in path.selected_nodes:
                if node.rank < node.tree_node.talent.max_rank:
                    potential_increments.append((node, node.tree_node))

            # print(f"potential increments: {potential_increments}")
            for old_selected, new_node in potential_increments:
                copied_selected_nodes = path.selected_nodes.copy()
                copied_selected_nodes.remove(old_selected)
                new_paths.append(
                    NodePath(
                        # might need a copy
                        selected_nodes=copied_selected_nodes
                        + [
                            SelectedTreeNode(
                                tree_node=new_node, rank=old_selected.rank + 1
                            )
                        ]
                    )
                )
            # print("new paths")
            # print(new_paths)

        return new_paths

    def _make_paths_unique(paths: typing.List[NodePath]) -> typing.List[NodePath]:
        """Ensure each path exists only once."""
        unique_paths: typing.Dict[str, NodePath] = {}
        for path in paths:
            names = set()
            for node in path.selected_nodes:
                name = node.tree_node.talent.full_name + str(node.rank)
                names.add(name)
            names = "".join(sorted(list(names)))
            unique_paths[names] = path

        return list(unique_paths.values())

    for point in range(1, points):
        # print(f"time to add point {point}")
        paths = _create_paths(paths=paths)
        paths = _make_paths_unique(paths)

    return paths
