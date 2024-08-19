"""
gastank — Today at 03:37
ya
still not sure where the talent -> spec mapping is. traittree.db2 seems to be just different versions of the tree instead of tree by spec
think that's where you sometimes get multiple entries in traitdef pointing to the same talent

Dorovon — Today at 03:43
SkillLineXTraitTree has class -> tree mappings it seems
TraitCond -> TraitNodeGroup seems to be spec mappings
using spec sets and not just specs

gastank — Today at 04:26
ok ya traitnode -> traitnodegroupxtraitnode -> traitnodegroupxtraitcond -> traitcond
so we can parse traitnode, filter out only current traittreeid and all the relevant info should flow out from there

navv — Today at 14:35
hm, i suppose the entrypoint for exporting has to be the skilllineXtraittree
that seems to be the place where class-specific stuff all begins



Anshlun — Today at 19:59
SkillLine 798 is "druid skills"
SkillLineXTraitTree 798 maps to tree 219
TraitNodeGroup for tree 219 has many groups, including 2128
# TraitNodeGroupXTraitNode for group 2128 has many nodes, including 17260
TraitNodeXTraitNodeEntry for 17260 maps to node entry 21826
TraitNodeEntry 21826 maps to definition 22202
TraitDefinition 22202 uses spell 278515
Spell 278515 is "Rampant Growth" - "Regrowth's healing over time is increased by x%, and it also applies to the target of your Lifebloom."



so a bit less cursed way is to make a tree map out of those
TraitNodeGroupXTraitCost gets you some of the way there automatically
curiously, not fully there which surprises me
i would have expected i could find every spell tagged with the left side cost for example



that's the ticket
trait tree -> trait tree x trait currency -> trait cost definition -> traitnodegroupxtraitcost
presuming index 1 in trait tree x trait currency is always the generic one, but i suspect that's a safe bet
Dorovon — Today at 11:47
yeah
for class trees anyway



navv — Today at 12:08
yep there we go
id=79 id_trait_node_group=901 id_trait_cost=172 id_parent=901
id=80 id_trait_node_group=907 id_trait_cost=173 id_parent=907
id=96 id_trait_node_group=1890 id_trait_cost=711 id_parent=1890
id=95 id_trait_node_group=1886 id_trait_cost=710 id_parent=1886
id=99 id_trait_node_group=1918 id_trait_cost=723 id_parent=1918
id=100 id_trait_node_group=1929 id_trait_cost=722 id_parent=1929
id=103 id_trait_node_group=2040 id_trait_cost=785 id_parent=2040
id=104 id_trait_node_group=2043 id_trait_cost=786 id_parent=2043
id=108 id_trait_node_group=2112 id_trait_cost=813 id_parent=2112
id=107 id_trait_node_group=2109 id_trait_cost=814 id_parent=2109
id=112 id_trait_node_group=2141 id_trait_cost=818 id_parent=2141
id=111 id_trait_node_group=2131 id_trait_cost=817 id_parent=2131
straight from SkillLineXTraitTree to the correct node groups for each "cost" (index 1 and 2)
so now only need to do a mapping from node group to index
nice
alright
well shit
tranquility does not map to any tree
it's the only thing that's lacking
either the "left side" or "right side"




navv — Today at 10:11
didn't really settle on anything final yet, mostly concentrated on trying to get a sensible list out of the system
but basically starts with SkillLineXTraitTree to figure out which trait trees to get
after that, TraitNodeGroup gets you all the node groups for those trees
and then various glue db2 files get you things related to those node groups
TraitNodeGroupXTraitNode gets you the trait nodes associated with the node group, TraitNodeGroupXTraitCond gets you trait conditions associated with the group
TraitNode has the nodes, then TraitNodeXTraitNodeCond gets you trait conditions associated with a specific node (druids use this or example to give spec specific starsurge spells)
then i jump through some hoops to figure out which trait tree is the left and which is the right
TraitNodes also get you to TraitNodeEntries (through TraitNodeXTraitNodeEntry) .. TraitNodeEntry is your actual trait at the end of the day
from the perspective of individual spells that we have, i basically collect the info atm into a (spell_id, trait_node_id) map, because the same spell can be associated with various trait nodes



there's still plenty to do tho this is just the traits, i need to hook it up so that we get the spells also etc
oh, and for the links between traits, TraitEdge has them, it links nodes
seems pretty straightforward to me
i didn't bother with that for now, and also didn't want to add point requirements for now
the point requirement thing makes life a bit more complicated really from exportation perspective



alright, traitcond values i guess are relatively simple to figure out
condition type 0 is point requirement
condition type 1 is spec override
condition type 2 is spec start
or spec freebie

"""

import logging
import typing
import os
import requests
import json

from .utils import (
    ArgsObject,
    _LOCALES,
    collect_localizations,
    get_localized_spell_names,
    DATA_PATH,
    LOCALE_TABLES,
    safely_convert_to,
)
from .extractor import Extractor

logger = logging.getLogger(__name__)


class TalentExtractor(Extractor):
    def __init__(self, user_args: ArgsObject) -> None:
        super().__init__(user_args)

        self.TALENTS = "Talent"
        self.SPELLS = "SpellName"

        self.other_tables = [
            "GarrTalent",
            "GarrTalentRank",
            "GarrTalentTree",
            "MinorTalent",
            "RelicTalent",
            "SpellName",
            "SkillLine",
            "SkillLineAbility",
            "SkillLineXTraitTree",
            "Talent",
            "TraitCond",
            "TraitCost",
            "TraitCostDefinition",
            "TraitCurrency",
            "TraitDefinition",
            "TraitDefinitionEffectPoints",
            "TraitNode",
            "TraitNodeEntry",
            "TraitNodeGroup",
            "TraitNodeGroupXTraitCond",
            "TraitNodeGroupXTraitCost",
            "TraitNodeGroupXTraitNode",
            "TraitNodeXTraitCond",
            "TraitNodeXTraitNodeEntry",
            "TraitTree",
            "TraitTreeXTraitCurrency",
        ]

    @property
    def tables(self) -> typing.List[str]:
        return [self.TALENTS, self.SPELLS]

    def combine_into_json(self, data: typing.Dict[str, LOCALE_TABLES]) -> None:
        talents = data[self.TALENTS][_LOCALES[0]]

        # instead of trusting the talent names in the talent table we trust only their spell names
        talent_spell_ids = list([talent["id_spell"] for talent in talents])
        localized_spells = collect_localizations(
            data[self.SPELLS],
            filter_function=lambda spell: spell["id"] in talent_spell_ids,
        )
        for talent in talents:
            localized_spell_names = get_localized_spell_names(
                localized_spells, safely_convert_to(talent["id_spell"], int, -1)
            )
            talent.update(localized_spell_names)

        with open(os.path.join(DATA_PATH, "talents.json"), "w", encoding="utf-8") as f:
            json.dump(talents, f, ensure_ascii=False)

        logger.info(f"Updated {len(talents)} talents")


class TalentLoader(Extractor):
    """Contrary to actual Extractors this one just loads the necessary data from raidbots.com.
    Thank you mate for allowing this. Endpoint and structure might change.
    """

    @property
    def tables(self) -> typing.List[str]:
        return []

    def combine_into_json(self, data: typing.Dict[str, LOCALE_TABLES]) -> None:
        # https://www.raidbots.com/static/data/live/talents.json
        # live
        # ptr
        # beta
        data_endpoint = ""
        if self.user_args.alpha:
            data_endpoint = "beta"
        elif self.user_args.beta:
            data_endpoint = "beta"
        elif self.user_args.ptr:
            data_endpoint = "xptr"
            logger.warning(
                f"Using {data_endpoint} endpoint. Make sure this matches the currently most updated PTR!"
            )
        else:
            data_endpoint = "live"

        url = f"https://www.raidbots.com/static/data/{data_endpoint}/talents.json"

        loaded_data = requests.get(url)
        if loaded_data.status_code != 200:
            logger.error(
                f"Couldn't load Talent information from raidbots. {loaded_data.status_code}: {loaded_data.reason}"
            )
        json_data = loaded_data.json()

        spellicon_wowhead_icon_map = {
            "spell_frost_piercing_chill": "spell_frost_piercing-chill",
            "spell_frost_ice_shards": "spell_frost_ice-shards",
            "spell_frost_ring_of_frost": "spell_frost_ring-of-frost",
            "spell_priest_power_word": "spell_priest_power-word",
            "inv_artifact_ashes_to_ashes": "inv_artifact_ashes-to-ashes",
            "spell_priest_void_flay": "spell_priest_void-flay",
            "spell_priest_shadow_mend": "spell_priest_shadow-mend",
            "spell_priest_void_blast": "spell_priest_void-blast",
            "spell_firefrost_orb": "spell_firefrost-orb",
            "spell_frostfire_orb": "spell_frostfire-orb",
            "ability_rogue_shuriken_storm": "ability_rogue_shuriken-storm",
            "warlock__healthstone": "warlock_-healthstone",
        }

        # save raw
        with open(
            r"simc_support\game_data\data_files\trees\raw_raidbots_talent_information.json",
            "w",
            encoding="utf-8",
        ) as f:
            json.dump(json_data, f, ensure_ascii=False)

        # save by class
        for spec_data in json_data:
            spec_name = spec_data["specName"].lower()
            try:
                class_name = spec_data["className"].lower()
            except KeyError:
                logger.warning(
                    f"Couldn't find className in talent data of a spec. Expecting this to be Evoker. specName is {spec_data['specName']}"
                )
                spec_data["className"] = "Evoker"
                class_name = "evoker"

            combined_name = "_".join([class_name, spec_name]).replace(" ", "_")

            for tree in ["specNodes", "classNodes"]:
                for node in spec_data[tree]:
                    for entry in node["entries"]:
                        # somehow icons started to get missing
                        if "icon" in entry:
                            entry["icon"] = spellicon_wowhead_icon_map.get(
                                entry["icon"], entry["icon"]
                            )

            # sanity/curiousity checks
            logger.info(
                f"{combined_name}: {len(spec_data['classNodes'])} class nodes, {len(spec_data['specNodes'])} spec nodes"
            )

            with open(
                rf"{DATA_PATH}\trees\{combined_name}.json",
                "w",
                encoding="utf-8",
            ) as f:
                json.dump(spec_data, f)
