import json
import logging
import pkg_resources
import typing
import enum
import datetime
import logging
import itertools
import dataclasses

from simc_support.game_data.Language import Translation, _get_translations
from simc_support.game_data.SimcObject import SimcObject, convert_to_simc_string

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

    @property
    def simc_name(self) -> str:
        return convert_to_simc_string(self.name)


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
        "order_index",
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
        order_index: int,
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
        # order_index repesents the index in a wow talent export string
        self.order_index: int = order_index

        # index within a talent list of a Tree
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
    __slots__ = (
        "spec_id",
        "tree_nodes",
        "full_node_order",
    )

    def __init__(
        self,
        spec_id: int,
        tree_nodes: typing.Tuple[TreeNode, ...],
        full_node_order: typing.List[int],
    ) -> None:
        self.spec_id: int = spec_id
        self.tree_nodes: typing.Tuple[TreeNode, ...] = tree_nodes
        self.full_node_order = full_node_order

        self._tree_nodes_post_init()

    def _tree_nodes_post_init(self) -> None:
        """Builds links between all TreeNodes and their parents and children

        Raises:
            InitializationError: if some links aren't symmetrical
        """

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
        logger.debug("Starting nodes", existing_paths)

        for invested_points in range(1, points + 1):
            start_time = datetime.datetime.utcnow()

            new_paths: typing.Dict[TreePath, typing.Set[TreeNode]] = {}

            for path, entry_points in existing_paths.items():

                for node in entry_points:
                    # # elemental shaman logic
                    # if invested_points > 20 and node.required_invested_points < 20:
                    #     continue

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


class TreePath:
    __slots__ = (
        "tree",
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
        tree: Tree,
        path: typing.Optional[typing.Tuple[int, ...]] = None,
        invested_points: typing.Optional[int] = None,
    ) -> None:
        self.tree: Tree = tree

        if path is None and invested_points is None:
            self.path: typing.Tuple[int, ...] = tuple(0 for _ in tree.tree_nodes)
            self.invested_points = 0
        elif path is not None and invested_points is not None:
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

        return TreePath(
            tree=self.tree, path=new_path, invested_points=self.invested_points + 1
        )

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

    def get_unpacked_paths(
        self,
    ) -> typing.Iterable[typing.Tuple[typing.Tuple[int, Talent], ...]]:
        """unpacks a tree path into all talent path variants (meaning: create a path for each selected choice node option)

        Returns:
            typing.Iterable[typing.Tuple[typing.Tuple[int, Talent], ...]]: paths[path((rank, Talent),...)]
        """
        # should by only one anyway
        base_nodes = [
            (self.get_rank(n), n.talents[0])
            for n in self.tree.tree_nodes
            if self.get_rank(n) > 0 and n.tree_node_type != TreeNodeType.CHOICE
        ]
        # grouped up nicely already
        unpackable_nodes = [
            n.talents
            for n in self.tree.tree_nodes
            if self.get_rank(n) > 0 and n.tree_node_type == TreeNodeType.CHOICE
        ]
        unpackable_ranks = [
            self.get_rank(n)
            for n in self.tree.tree_nodes
            if self.get_rank(n) > 0 and n.tree_node_type == TreeNodeType.CHOICE
        ]
        unpacked_path_parts: itertools.product[typing.Tuple[Talent, ...]] = (
            itertools.product(*unpackable_nodes)
        )
        rank_and_parts = [
            tuple(zip(unpackable_ranks, part)) for part in unpacked_path_parts
        ]
        paths = [(*base_nodes, *part) for part in rank_and_parts]
        return paths


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
        order = loaded_talents[spec]["fullNodeOrder"]
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
                        order_index=order.index(raw_node["id"]),
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
                if not raw_talent:
                    continue

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
                    max_rank=raw_node.get("maxRanks", 1),
                    children_ids=tuple(raw_node["next"]),
                    talents=tuple(talents),
                    order_index=order.index(raw_node["id"]),
                )
            )

        class_tree = Tree(
            spec_id=loaded_talents[spec]["specId"],
            tree_nodes=tuple(class_nodes),
            full_node_order=order,
        )
        spec_tree = Tree(
            spec_id=loaded_talents[spec]["specId"],
            tree_nodes=tuple(spec_nodes),
            full_node_order=order,
        )

        trees[spec] = (class_tree, spec_tree)

    return trees


TREES: typing.Dict[str, typing.Tuple[Tree, Tree]] = _load_talents(_load_talent_files())

# Blizzard talent string sources:
#
# https://github.com/Gethe/wow-ui-source/blob/beta/Interface/AddOns/Blizzard_ClassTalentUI/Blizzard_ClassTalentImportExport.lua
# https://github.com/simulationcraft/simc/blob/dragonflight/engine/player/player.cpp#L2469


def get_trees_by_spec_id(spec_id: int) -> typing.Tuple[Tree, Tree]:
    """_summary_

    Args:
        spec_id (int): _description_

    Returns:
        typing.Tuple[Tree, Tree]: class_tree, spec_tree
    """
    for class_tree, spec_tree in TREES.values():
        if class_tree.spec_id == spec_id:
            return (class_tree, spec_tree)
    raise ValueError(f"No trees found for spec with id '{spec_id}'.")


def get_nodes_from_wow_export_string(wow_export_string: str) -> typing.List[TreeNode]:
    # .\engine\player\player.cpp:2470
    BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    # hardcoded values from Interface/AddOns/Blizzard_ClassTalentUI/Blizzard_ClassTalentImportExport.lua
    LOADOUT_SERIALIZATION_VERSION = 1
    # serialization version
    VERSION_BITS = 8
    # specialization id
    SPEC_BITS = 16
    # C_Traits.GetTreeHash(), optionally can be 0-filled
    TREE_BITS = 128
    # ranks purchased if node is partially filled
    RANK_BITS = 6
    # choice index, 0-based
    CHOICE_BITS = 2
    # hardcoded value from Interface/SharedXML/ExportUtil.lua
    BYTE_SIZE = 6

    def convert_into_indexes(string: str) -> typing.List[int]:
        numbers = []
        for letter in string:
            numbers.append(BASE64_CHARS.index(letter))
        return numbers

    def convert_into_bin(numbers: typing.List[int]) -> typing.List[str]:
        bins = []
        for number in numbers:
            bins.append(f"{number:06b}")
        return bins

    def extract_version(inverse_binary_strings: typing.List[str]) -> int:
        """
        Description:
        so the header starts <version:8bit>|<specid:16bit>, which encoded for balance druid (version 1|spec 102) is BYGA. base64decoded into binary that gives
        ```
        binary:   000001 011000 000110 000000
        position: 123456 789012 345678 901234
        ```

        but when contructing the first 8bit they take bits 11 & 12 then concat bits 1->6, so it looks like
        ```
        binary:   00 000001 = 1
        position: 12 123456
        ```

        Args:
            binary_string (str): _description_

        Returns:
            int: _description_
        """
        bin_string = "".join(inverse_binary_strings)
        bits = bin_string[-VERSION_BITS:]
        return int(bits, 2)

    def extract_spec_id(inverse_binary_strings: typing.List[str]) -> int:
        """
        Description:
        so the header starts <version:8bit>|<specid:16bit>, which encoded for balance druid (version 1|spec 102) is BYGA. base64decoded into binary that gives
        ```
        binary:   000001 011000 000110 000000
        position: 123456 789012 345678 901234
        ```

        then for the next 16 bits they starts from bit 19->24, then 13->18, then 7->10
        ```
        binary:   000000 000110 0110 = 102
        position: 901234 345678 7890
        ```

        Args:
            binary_string (str): _description_

        Returns:
            int: _description_
        """
        bin_string = "".join(inverse_binary_strings)
        bits = bin_string[-SPEC_BITS - VERSION_BITS : -VERSION_BITS]
        return int(bits, 2)

    @dataclasses.dataclass
    class ExtractedNode:
        node_id: int
        talent_info: str
        trees: typing.Tuple[Tree, Tree]

        @property
        def is_selected(self) -> bool:
            return self.talent_info[0] == "1"

        @property
        def node(self) -> TreeNode:
            nodes = list(self.trees[0].tree_nodes) + list(self.trees[1].tree_nodes)
            return self._get_tree_node_by_node_id(self.node_id, nodes)

        @property
        def rank(self) -> int:
            if not self.is_selected:
                return 0
            if self.talent_info[1] == "0":
                return self.node.max_rank
            return int(self.talent_info[2 : 2 + 6], 2)

        @property
        def is_choice_node(self) -> bool:
            if not self.is_selected:
                return False

            choice_bit = 2 if self.talent_info[1] == "0" else 9

            return self.talent_info[choice_bit] == "1"

        @property
        def talent_index(self) -> int:
            talent_bit_start = 3 if self.talent_info[1] == "0" else 10
            talent_bits = 2
            return int(
                self.talent_info[talent_bit_start : talent_bit_start + talent_bits], 2
            )

        @property
        def talent(self) -> Talent:
            return self.node.talents[self.talent_index]

        def _get_tree_node_by_node_id(
            self, node_id: int, nodes: typing.List[TreeNode]
        ) -> TreeNode:
            for node in nodes:
                if node.id == node_id:
                    node.rank = self.rank
                    return node
            raise ValueError(f"TreeNode for ID {node_id} was not found in spec.")

    def extract_talent_info(
        inverse_binary_strings: typing.List[str],
    ) -> typing.List[str]:
        """_summary_

        Args:
            inverse_binary_strings (typing.List[str]): _description_

        Returns:
            typing.List[str]: list of 11 bit strings, e.g. ["00000000000", "10000000000"]
        """

        def yield_info(info_string: str) -> typing.Generator[str, str, None]:
            """
            1 bit = is node taken?
                1 bit = is node partial?
                    6 bit = ranks if not full
                1 bit = is node choice
                    2 bit = choice index

            Args:
                info_string (str): _description_

            Returns:
                str: _description_
            """
            copy_str = info_string
            while len(copy_str) > 0:
                offset = 0

                # taken?
                offset += 1
                talent_info = copy_str[-offset]
                if copy_str[-offset] == "1":

                    # partial?
                    offset += 1
                    talent_info += copy_str[-offset]
                    if copy_str[-offset] == "1":
                        talent_info += copy_str[-RANK_BITS - offset : -offset]
                        offset += RANK_BITS

                    # is choice node
                    offset += 1
                    talent_info += copy_str[-offset]
                    if copy_str[-offset] == "1":
                        talent_info += copy_str[-CHOICE_BITS - offset : -offset]
                        offset += CHOICE_BITS

                # print(f"yielding and offset of {offset} with string '{talent_info}'")
                yield talent_info

                copy_str = copy_str[:-offset]

        bin_string = "".join(inverse_binary_strings)

        talent_bin_string = bin_string[: -TREE_BITS - SPEC_BITS - VERSION_BITS]

        info = []
        for index, talent_info in enumerate(yield_info(talent_bin_string)):
            full_talent_info = f"{talent_info:0<11}"
            info.append(full_talent_info)
            # print(index, full_talent_info)
        return info

    def get_extracted_nodes(
        talent_info: typing.List[str], trees: typing.Tuple[Tree, Tree]
    ) -> typing.List[ExtractedNode]:
        talents: typing.List[ExtractedNode] = []
        full_node_order = trees[0].full_node_order
        for info, node_id in zip(talent_info, full_node_order):
            talents.append(
                ExtractedNode(node_id=node_id, talent_info=info, trees=trees)
            )

        return talents

    indexes = convert_into_indexes(wow_export_string)
    # print(numbers)
    binary_strings = convert_into_bin(indexes)
    # print(binary_strings)
    inverse_binary_strings = binary_strings[::-1]
    # print(inverse_binary_strings)

    # unnecessary for now
    string_version = extract_version(inverse_binary_strings)
    # print(string_version)

    spec_id = extract_spec_id(inverse_binary_strings)
    # print(spec_id)

    trees = get_trees_by_spec_id(spec_id)

    talent_info = extract_talent_info(inverse_binary_strings)

    nodes = get_extracted_nodes(talent_info, trees)

    for node in nodes:
        if node.is_selected:
            print(f"{node.rank} {node.talent.name}")

    return [n.node for n in nodes]
