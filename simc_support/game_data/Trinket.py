
from .ItemLevel import *
from . import Source

class Trinket(object):
    """docstring for trinket"""

    def __init__(
        self,
        name,
        item_id,
        min_itemlevel,
        max_itemlevel,
        max_itemlevel_drop,
        agility,
        intellect,
        strength,
        melee,
        ranged,
        legendary=False,
        source=None,
        active=False
    ):
        super(Trinket, self).__init__()
        self.name: str = str(name)
        self.item_id: str = str(item_id)
        self.min_itemlevel: int = int(min_itemlevel)
        self.max_itemlevel: int = int(max_itemlevel)
        self.max_itemlevel_drop: int = int(max_itemlevel_drop)
        self.agility: bool = bool(agility)
        self.intellect: bool = bool(intellect)
        self.strength: bool = bool(strength)
        self.melee: bool = bool(melee)
        self.ranged: bool = bool(ranged)
        self.legendary: bool = bool(legendary)
        self.source: str = str(source)
        self.active: bool = bool(active)

    def get_name(self):
        return self.name

    def get_id(self):
        return self.item_id

    def get_source(self):
        return self.source



trinket_list = [
    # dungeon trinkets
    Trinket( # atal'dazar
        "My'das Talisman", "158319", DUNGEON_ITEMLEVEL, M_PLUS_ITEMLEVEL+TITANFORGING_CUT_OFF,
        TRADER_TOKEN, True, False, False, False, False, source=Source.DUNGEON, active=True
    ),
    Trinket( # atal'dazar
        "Rezan's Gleaming Eye", "158712", DUNGEON_ITEMLEVEL, M_PLUS_ITEMLEVEL+TITANFORGING_CUT_OFF,
        TRADER_TOKEN, False, False, True, False, False, source=Source.DUNGEON, active=False
    ),
    Trinket( # atal'dazar
        "Vessel of Skittering Shadows", "159610", DUNGEON_ITEMLEVEL,
        M_PLUS_ITEMLEVEL+TITANFORGING_CUT_OFF, TRADER_TOKEN, False, True, False, False, False, source=Source.DUNGEON, active=False
    ),
    Trinket( # freehold
        "Harlan's Loaded Dice", "155881", DUNGEON_ITEMLEVEL, M_PLUS_ITEMLEVEL+TITANFORGING_CUT_OFF,
        TRADER_TOKEN, True, False, False, False, False, source=Source.DUNGEON, active=False
    ),
    Trinket( # Kings' Rest
        "Lustrous Golden Plumage", "159617", DUNGEON_ITEMLEVEL, M_PLUS_ITEMLEVEL+TITANFORGING_CUT_OFF,
        TRADER_TOKEN, True, False, False, False, False, source=Source.DUNGEON, active=True
    ),
    Trinket( # Shrine of the Storm
        "Briny Barnacle", "159619", DUNGEON_ITEMLEVEL, M_PLUS_ITEMLEVEL+TITANFORGING_CUT_OFF,
        TRADER_TOKEN, False, False, True, False, False, source=Source.DUNGEON, active=False
    ),
    Trinket( # Shrine of the Storm
        "Galecaller's Boon", "159614", DUNGEON_ITEMLEVEL, M_PLUS_ITEMLEVEL+TITANFORGING_CUT_OFF,
        TRADER_TOKEN, True, False, False, False, False, source=Source.DUNGEON, active=True
    ),
    Trinket( # Shrine of the Storm
        "Conch of Dark Whispers", "159620", DUNGEON_ITEMLEVEL, M_PLUS_ITEMLEVEL+TITANFORGING_CUT_OFF,
        TRADER_TOKEN, False, True, False, False, False, source=Source.DUNGEON, active=False
    ),
    Trinket( # Siege of Boralus
        "Dead-Eye Spyglass", "159623", DUNGEON_ITEMLEVEL, M_PLUS_ITEMLEVEL+TITANFORGING_CUT_OFF,
        TRADER_TOKEN, True, False, False, False, False, source=Source.DUNGEON, active=False
    ),
    Trinket( # Siege of Boralus
        "Hadal's Nautilus", "159622", DUNGEON_ITEMLEVEL, M_PLUS_ITEMLEVEL+TITANFORGING_CUT_OFF,
        TRADER_TOKEN, False, True, False, False, False, source=Source.DUNGEON, active=False
    ),
    Trinket( # Temple of Sethraliss
        "Tiny Electromental in a Jar", "158374", DUNGEON_ITEMLEVEL, M_PLUS_ITEMLEVEL+TITANFORGING_CUT_OFF,
        TRADER_TOKEN, True, False, False, False, False, source=Source.DUNGEON, active=False
    ),
    Trinket( # Temple of Sethraliss
        "Merektha's Fang", "158367", DUNGEON_ITEMLEVEL, M_PLUS_ITEMLEVEL+TITANFORGING_CUT_OFF,
        TRADER_TOKEN, False, False, True, False, False, source=Source.DUNGEON, active=True
    ),
    Trinket( # The Motherlode
        "Razdunk's Big Red Button", "159611", DUNGEON_ITEMLEVEL, M_PLUS_ITEMLEVEL+TITANFORGING_CUT_OFF,
        TRADER_TOKEN, False, False, True, False, False, source=Source.DUNGEON, active=True
    ),
    Trinket( # The Motherlode
        "Azerokk's Resonating Heart", "159612", DUNGEON_ITEMLEVEL, M_PLUS_ITEMLEVEL+TITANFORGING_CUT_OFF,
        TRADER_TOKEN, True, False, False, False, False, source=Source.DUNGEON, active=False
    ),
    Trinket( # The Underrot
        "Lingering Sporepods", "159626", DUNGEON_ITEMLEVEL, M_PLUS_ITEMLEVEL+TITANFORGING_CUT_OFF,
        TRADER_TOKEN, True, False, True, False, False, source=Source.DUNGEON, active=False
    ),
    Trinket( # The Underrot
        "Rotcrusted Voodoo Doll", "159624", DUNGEON_ITEMLEVEL, M_PLUS_ITEMLEVEL+TITANFORGING_CUT_OFF,
        TRADER_TOKEN, False, True, False, False, False, source=Source.DUNGEON, active=True
    ),
    Trinket( # The Underrot
        "Vial of Animated Blood", "159625", DUNGEON_ITEMLEVEL, M_PLUS_ITEMLEVEL+TITANFORGING_CUT_OFF,
        TRADER_TOKEN, False, False, True, False, False, source=Source.DUNGEON, active=True
    ),
    Trinket( # Tol Dagor
        "Jes' Howler", "159627", DUNGEON_ITEMLEVEL, M_PLUS_ITEMLEVEL+TITANFORGING_CUT_OFF, TRADER_TOKEN,
        False, False, True, False, False, source=Source.DUNGEON, active=True
    ),
    Trinket( # Tol Dagor
        "Ignition Mage's Fuse", "159615", DUNGEON_ITEMLEVEL, M_PLUS_ITEMLEVEL+TITANFORGING_CUT_OFF,
        TRADER_TOKEN, False, True, False, False, False, source=Source.DUNGEON, active=True
    ),
    Trinket( # Waycrest Manor
        "Lady Waycrest's Music Box", "159631", DUNGEON_ITEMLEVEL, M_PLUS_ITEMLEVEL+TITANFORGING_CUT_OFF,
        TRADER_TOKEN, False, True, False, False, False, source=Source.DUNGEON, active=False
    ),
    Trinket( # Waycrest Manor
        "Balefire Branch", "159630", DUNGEON_ITEMLEVEL, M_PLUS_ITEMLEVEL+TITANFORGING_CUT_OFF,
        TRADER_TOKEN, False, True, False, False, False, source=Source.DUNGEON, active=True
    ),
    # Trinket( # not obtainable
    #     "Cursed Captain's Charm", "161115", 290, TITANFORGE_CAP,
    #     TRADER_TOKEN, True, True, True, False, False, active=False
    # ),
    Trinket( # world boss
        "Azurethos' Singed Plumage", "161377", 355, 355+TITANFORGING_CUT_OFF, TRADER_TOKEN,
        False, True, False, False, False, source=Source.WORLD_BOSS, active=True
    ),
    Trinket( # world boss
        "Drust-Runed Icicle", "161380", 355, 355+TITANFORGING_CUT_OFF, TRADER_TOKEN, False,
        True, False, False, False, source=Source.WORLD_BOSS, active=False
    ),
    # Trinket( # ???
    #     "Dunewalker's Survival Kit", "161418", 340, TITANFORGE_CAP, TRADER_TOKEN,
    #     True, False, False, False, False, active=True
    # ),
    Trinket( # world boss
        "Galecaller's Beak", "161379", 355, 355+TITANFORGING_CUT_OFF, TRADER_TOKEN, False,
        False, True, False, False, source=Source.WORLD_BOSS, active=True
    ),
    Trinket( # world boss
        "Kraulok's Claw", "161419", 355, 355+TITANFORGING_CUT_OFF, TRADER_TOKEN, False,
        False, True, False, False, source=Source.WORLD_BOSS, active=False
    ),
    Trinket( # world boss
        "Permafrost-Encrusted Heart", "161381", 355, 355+TITANFORGING_CUT_OFF, TRADER_TOKEN,
        True, False, False, False, False, source=Source.WORLD_BOSS, active=False
    ),
    Trinket( # world boss
        "Plume of the Seaborne Avian", "161378", 355, 355+TITANFORGING_CUT_OFF, TRADER_TOKEN,
        True, False, False, False, False, source=Source.WORLD_BOSS, active=False
    ),
    Trinket( # world boss
        "Prism of Dark Intensity", "161376", 355, 355+TITANFORGING_CUT_OFF, TRADER_TOKEN,
        False, False, True, False, False, source=Source.WORLD_BOSS, active=False
    ),
    Trinket( # world boss
        "Spiritbound Voodoo Burl", "161412", 355, 355+TITANFORGING_CUT_OFF, TRADER_TOKEN, True,
        False, False, False, False, source=Source.WORLD_BOSS, active=False
    ),
    Trinket( # world boss
        "T'zane's Barkspines", "161411", 355, 355+TITANFORGING_CUT_OFF, TRADER_TOKEN, False,
        True, False, False, False, source=Source.WORLD_BOSS, active=True
    ),
    Trinket( # inscription
        "Darkmoon Deck: Squalls", "159126", 355, 355,
        355, False, True, False, False, False, source=Source.PROFESSION, active=False
    ),
    Trinket( # inscription
        "Darkmoon Deck: Fathoms", "159125", 355, 355,
        355, True, False, True, False, False, source=Source.PROFESSION, active=False
    ),
    Trinket( # alchemy
        "Surging Alchemist Stone", "152632", 300, 300,
        300, True, True, True, False, False, source=Source.PROFESSION, active=False
    ),
    Trinket( # world quest
        "Plunderbeard's Flask", "158164", WORLD_QUEST_ITEMLEVEL, WORLD_QUEST_ITEMLEVEL+TITANFORGING_CUT_OFF,
        TRADER_TOKEN, True, True, True, False, False, source=Source.WORLD_QUEST, active=True
    ),
    Trinket( # Uldir
        "Frenetic Corpuscle", "160648", 340, ULDIR+TITANFORGING_CUT_OFF,
        TRADER_TOKEN, True, False, False, False, False, source=Source.RAID, active=False
    ),
    Trinket( # Uldir
        "Construct Overcharger", "160652", 340, ULDIR+TITANFORGING_CUT_OFF,
        TRADER_TOKEN, True, False, False, False, False, source=Source.RAID, active=False
    ),
    Trinket(  # Uldir
        "Vigilant's Bloodshaper", "160651", 340, ULDIR+TITANFORGING_CUT_OFF,
        TRADER_TOKEN, False, True, False, False, False, source=Source.RAID, active=False
    ),
    Trinket( # Tol Dagor
        name="Kul Tiran Cannonball Runner", item_id="159628", min_itemlevel=DUNGEON_ITEMLEVEL, max_itemlevel=M_PLUS_ITEMLEVEL+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=False, strength=False, melee=False, ranged=False, source=Source.DUNGEON, active=False
    ),
    Trinket(  # Uldir
        name="Vanquished Tendril of G'huun", item_id="160654", min_itemlevel=340, max_itemlevel=ULDIR+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source=Source.RAID, active=False
    ),
    Trinket(  # world drop
        name="Landoi's Scrutiny", item_id="163935", min_itemlevel=350, max_itemlevel=350+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=False, strength=False, melee=False, ranged=False, source=Source.WORLD_DROP, active=False
    ),
    Trinket(  # world drop
        name="'Bygone Bee' Almanac", item_id="163936", min_itemlevel=350, max_itemlevel=350+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=False, intellect=False, strength=True, melee=False, ranged=False, source=Source.WORLD_DROP, active=True
    ),
    Trinket(  # world drop
        name="Leyshock's Grand Compilation", item_id="163937", min_itemlevel=350, max_itemlevel=350+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=False, intellect=True, strength=False, melee=False, ranged=False, source=Source.WORLD_DROP, active=False
    ),
    Trinket( # wq
        name="Kaja-fied Banana", item_id="161125", min_itemlevel=WORLD_QUEST_ITEMLEVEL, max_itemlevel=WORLD_QUEST_ITEMLEVEL+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source=Source.WORLD_QUEST, active=False
    ),
    Trinket(  # uldir
        name="Syringe of Bloodborne Infirmity", item_id="160655", min_itemlevel=340, max_itemlevel=ULDIR+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=False, intellect=False, strength=True, melee=False, ranged=False, source=Source.RAID, active=False
    ),
    Trinket(  # uldir
        name="Disc of Systematic Regression", item_id="160650", min_itemlevel=340, max_itemlevel=ULDIR+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=False, intellect=False, strength=True, melee=False, ranged=False, source=Source.RAID, active=False
    ),
    Trinket(  # uldir
        name="Twitching Tentacle of Xalzaix", item_id="160656", min_itemlevel=340, max_itemlevel=ULDIR+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=False, intellect=True, strength=False, melee=False, ranged=False, source=Source.RAID, active=False
    ),
    Trinket(  # alchemy
        name="Endless Tincture of Fractional Power", item_id="152636", min_itemlevel=300, max_itemlevel=300,
        max_itemlevel_drop=300, agility=True, intellect=True, strength=True, melee=True, ranged=True, source=Source.PROFESSION, active=True
    ),
    Trinket(  # stormsong valley
        name="Galewind Chimes", item_id="155568", min_itemlevel=WORLD_QUEST_ITEMLEVEL, max_itemlevel=WORLD_QUEST_ITEMLEVEL+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source=Source.WORLD_QUEST, active=False
    ),
    Trinket(  # wq
        name="Gilded Loa Figurine", item_id="158153", min_itemlevel=WORLD_QUEST_ITEMLEVEL, max_itemlevel=WORLD_QUEST_ITEMLEVEL+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source=Source.WORLD_QUEST, active=False
    ),
    Trinket(  # wq
        name="Emblem of Zandalar", item_id="158154", min_itemlevel=280, max_itemlevel=WORLD_QUEST_ITEMLEVEL+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source=Source.WORLD_QUEST, active=False
    ),
    Trinket(  # wq
        name="Dinobone Charm", item_id="158155", min_itemlevel=280, max_itemlevel=WORLD_QUEST_ITEMLEVEL+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source=Source.WORLD_QUEST, active=False
    ),
    Trinket(  # wq
        name="Pearl Diver's Compass", item_id="158162", min_itemlevel=280, max_itemlevel=WORLD_QUEST_ITEMLEVEL+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source=Source.WORLD_QUEST, active=True
    ),
    Trinket(  # wq
        name="First Mate's Spyglass", item_id="158163", min_itemlevel=280, max_itemlevel=WORLD_QUEST_ITEMLEVEL+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source=Source.WORLD_QUEST, active=True
    ),
    Trinket(  # stormsong valley
        name="Whirlwing's Plumage", item_id="158215", min_itemlevel=310, max_itemlevel=WORLD_QUEST_ITEMLEVEL+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source=Source.WORLD_QUEST, active=True
    ),
    Trinket(  # stormsong valley
        name="Living Oil Cannister", item_id="158216", min_itemlevel=310, max_itemlevel=WORLD_QUEST_ITEMLEVEL+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source=Source.WORLD_QUEST, active=True
    ),
    # Trinket(  # stormsong valley - tank
    #     name="Dadalea's Wing", item_id="158218", min_itemlevel=310, max_itemlevel=TITANFORGE_CAP,
    #     max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, active=False
    # ),
    Trinket(  # stormsong valley
        name="Vial of Storms", item_id="158224", min_itemlevel=310, max_itemlevel=WORLD_QUEST_ITEMLEVEL+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source=Source.WORLD_QUEST, active=True
    ),
    Trinket(  # stormsong valley
        name="Doom Shroom", item_id="158555", min_itemlevel=310, max_itemlevel=WORLD_QUEST_ITEMLEVEL+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source=Source.WORLD_QUEST, active=False
    ),
    Trinket(  # waycrest manor
        name="Gore-Crusted Butcher's Block", item_id="159616", min_itemlevel=DUNGEON_ITEMLEVEL, max_itemlevel=M_PLUS_ITEMLEVEL+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=False, intellect=False, strength=True, melee=False, ranged=False, source=Source.DUNGEON, active=False
    ),
    Trinket(  # stormsong valley
        name="Snowpelt Mangler", item_id="160263", min_itemlevel=310, max_itemlevel=WORLD_QUEST_ITEMLEVEL+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source=Source.WORLD_QUEST, active=False
    ),
    Trinket(  # nazmir
        name="Incessantly Ticking Clock", item_id="161113", min_itemlevel=325, max_itemlevel=WORLD_QUEST_ITEMLEVEL+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source=Source.WORLD_QUEST, active=False
    ),
    Trinket(  # vol'dun
        name="Ravasaur Skull Bijou", item_id="161119", min_itemlevel=325, max_itemlevel=WORLD_QUEST_ITEMLEVEL+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source=Source.WORLD_QUEST, active=False
    ),
    Trinket(  # nazmir
        name="Crawg Gnawed Femur", item_id="163703", min_itemlevel=325, max_itemlevel=WORLD_QUEST_ITEMLEVEL+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source=Source.WORLD_QUEST, active=False
    ),
    Trinket(  # airdrop
        name="Dread Gladiator's Badge", item_id="161902", min_itemlevel=325, max_itemlevel=M_PLUS_ITEMLEVEL+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source="PvP", active=True
    ),
    Trinket(  # warfront world boss
        name="Lion's Grace", item_id="161472", min_itemlevel=370, max_itemlevel=370+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=False, intellect=True, strength=False, melee=False, ranged=False, source=Source.WORLD_BOSS, active=False
    ),
    Trinket(  # warfront world boss
        name="Lion's Guile", item_id="161473", min_itemlevel=370, max_itemlevel=370+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=False, strength=False, melee=False, ranged=False, source=Source.WORLD_BOSS, active=True
    ),
    Trinket(  # warfront world boss
        name="Lion's Strength", item_id="161474", min_itemlevel=370, max_itemlevel=370+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=False, intellect=False, strength=True, melee=False, ranged=False, source=Source.WORLD_BOSS, active=True
    ),
    Trinket(  # warfront world boss
        name="Doom's Fury", item_id="161463", min_itemlevel=370, max_itemlevel=370+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=False, intellect=False, strength=True, melee=False, ranged=False, source=Source.WORLD_BOSS, active=True
    ),
    Trinket(  # warfront world boss
        name="Doom's Hatred", item_id="161461", min_itemlevel=370, max_itemlevel=370+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=False, intellect=True, strength=False, melee=False, ranged=False, source=Source.WORLD_BOSS, active=False
    ),
    Trinket(  # warfront world boss
        name="Doom's Wake", item_id="161462", min_itemlevel=370, max_itemlevel=370+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=False, strength=False, melee=False, ranged=False, source=Source.WORLD_BOSS, active=True
    ),
    Trinket(  # pvp
        name="Dread Gladiator's Insignia", item_id="161676", min_itemlevel=280, max_itemlevel=M_PLUS_ITEMLEVEL+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source="PvP", active=False
    ),
    Trinket(  # pvp
        name="Dread Gladiator's Medallion", item_id="161674", min_itemlevel=280, max_itemlevel=M_PLUS_ITEMLEVEL+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source="PvP", active=True
    ),
    Trinket(  # wq
        name="Berserker's Juju", item_id="161117", min_itemlevel=280, max_itemlevel=WORLD_QUEST_ITEMLEVEL+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=TRADER_TOKEN, agility=True, intellect=True, strength=True, melee=True, ranged=True, source=Source.WORLD_QUEST, active=True
    ),
    Trinket(  # profession alchemy
        name="Sanguinated Alchemist Stone", item_id="166974", min_itemlevel=355, max_itemlevel=355,
        max_itemlevel_drop=355, agility=True, intellect=True, strength=True, melee=True, ranged=True, source=Source.PROFESSION, active=False
    ),
    Trinket(  # profession alchemy
        name="Tidal Alchemist Stone", item_id="165926", min_itemlevel=385, max_itemlevel=385,
        max_itemlevel_drop=385, agility=True, intellect=True, strength=True, melee=True, ranged=True, source=Source.PROFESSION, active=False
    ),
    Trinket(  # profession alchemy
        name="Spirited Alchemist Stone", item_id="165927", min_itemlevel=400, max_itemlevel=400,
        max_itemlevel_drop=385, agility=True, intellect=True, strength=True, melee=True, ranged=True, source=Source.PROFESSION, active=False
    ),
    Trinket(  # profession alchemy
        name="Eternal Alchemist Stone", item_id="165928", min_itemlevel=415, max_itemlevel=415,
        max_itemlevel_drop=415, agility=True, intellect=True, strength=True, melee=True, ranged=True, source=Source.PROFESSION, active=False
    ),
    Trinket(  # profession alchemy
        name="Crushing Alchemist Stone", item_id="168675", min_itemlevel=425, max_itemlevel=430,
        max_itemlevel_drop=425, agility=True, intellect=True, strength=True, melee=True, ranged=True, source=Source.PROFESSION, active=False
    ),
    Trinket(  # World Boss Dark Shore
        name="Ancient Knot of Wisdom", item_id="161417", min_itemlevel=355, max_itemlevel=355+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=355, agility=False, intellect=True, strength=False, melee=False, ranged=False, source=Source.WORLD_BOSS, active=True
    ),
    Trinket(  # World Boss Dark Shore
        name="Forest Lord's Razorleaf", item_id="166794", min_itemlevel=355, max_itemlevel=355+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=355, agility=True, intellect=False, strength=False, melee=False, ranged=False, source=Source.WORLD_BOSS, active=False
    ),
    Trinket(  # World Boss Dark Shore
        name="Knot of Ancient Fury", item_id="161413", min_itemlevel=355, max_itemlevel=355+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=355, agility=False, intellect=False, strength=True, melee=False, ranged=False, source=Source.WORLD_BOSS, active=True
    ),
    Trinket(  # Emissary
        name="Razzashi Tooth Medallion", item_id="165667", min_itemlevel=EMISSARY, max_itemlevel=EMISSARY+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=EMISSARY, agility=True, intellect=False, strength=False, melee=False, ranged=False, source=Source.WORLD_QUEST, active=False
    ),
    Trinket(  # Emissary
        name="Moonstone of Zin-Azshari", item_id="165666", min_itemlevel=EMISSARY, max_itemlevel=EMISSARY+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=EMISSARY, agility=False, intellect=True, strength=False, melee=False, ranged=False, source=Source.WORLD_QUEST, active=False
    ),
    Trinket(  # Emissary
        name="Ancient Tuskarr Sea Charm", item_id="165661", min_itemlevel=EMISSARY, max_itemlevel=EMISSARY+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=EMISSARY, agility=False, intellect=False, strength=True, melee=False, ranged=False, source=Source.WORLD_QUEST, active=False
    ),
    Trinket(  # Emissary
        name="Sea Giant's Tidestone", item_id="165664", min_itemlevel=EMISSARY, max_itemlevel=EMISSARY+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=EMISSARY, agility=False, intellect=True, strength=False, melee=False, ranged=False, source=Source.WORLD_QUEST, active=True
    ),
    Trinket(  # Emissary
        name="Kezan Stamped Bijou", item_id="165662", min_itemlevel=EMISSARY, max_itemlevel=EMISSARY+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=EMISSARY, agility=True, intellect=False, strength=False, melee=False, ranged=False, source=Source.WORLD_QUEST, active=True
    ),
    Trinket(  # Emissary
        name="Chargestone of the Thunder King's Court", item_id="165660", min_itemlevel=EMISSARY, max_itemlevel=EMISSARY+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=EMISSARY, agility=True, intellect=False, strength=False, melee=False, ranged=False, source=Source.WORLD_QUEST, active=False
    ),
    Trinket(  # Emissary
        name="Ritual Feather of Unng Ak", item_id="165665", min_itemlevel=EMISSARY, max_itemlevel=EMISSARY+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=EMISSARY, agility=False, intellect=False, strength=True, melee=False, ranged=False, source=Source.WORLD_QUEST, active=True
    ),
    Trinket(  # Dazar'Alor
        name="Crest of Pa'ku", item_id="166418", min_itemlevel=370, max_itemlevel=DAZARALOR+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=DAZARALOR, agility=False, intellect=True, strength=False, melee=False, ranged=False, source=Source.RAID, active=False
    ),
    Trinket(  # Dazar'Alor
        name="Everchill Anchor", item_id="165570", min_itemlevel=370, max_itemlevel=DAZARALOR+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=DAZARALOR, agility=False, intellect=False, strength=True, melee=False, ranged=False, source=Source.RAID, active=False
    ),
    Trinket(  # Dazar'Alor
        name="Grong's Primal Rage", item_id="165574", min_itemlevel=370, max_itemlevel=DAZARALOR+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=DAZARALOR, agility=False, intellect=False, strength=True, melee=False, ranged=False, source=Source.RAID, active=True
    ),
    Trinket(  # Dazar'Alor
        name="Incandescent Sliver", item_id="165571", min_itemlevel=370, max_itemlevel=DAZARALOR+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=DAZARALOR, agility=False, intellect=True, strength=False, melee=False, ranged=False, source=Source.RAID, active=False
    ),
    Trinket(  # Dazar'Alor
        name="Invocation of Yu'lon", item_id="165568", min_itemlevel=370, max_itemlevel=DAZARALOR+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=DAZARALOR, agility=True, intellect=False, strength=False, melee=False, ranged=False, source=Source.RAID, active=True
    ),
    Trinket(  # Dazar'Alor
        name="Kimbul's Razor Claw", item_id="165579", min_itemlevel=370, max_itemlevel=DAZARALOR+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=DAZARALOR, agility=True, intellect=False, strength=False, melee=False, ranged=False, source=Source.RAID, active=False
    ),
    Trinket(  # Dazar'Alor
        name="Rampaging Amplitude Gigavolt Engine", item_id="165580", min_itemlevel=370, max_itemlevel=DAZARALOR+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=DAZARALOR, agility=False, intellect=False, strength=True, melee=False, ranged=False, source=Source.RAID, active=True
    ),
    Trinket(  # Dazar'Alor
        name="Tidestorm Codex", item_id="165576", min_itemlevel=370, max_itemlevel=DAZARALOR+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=DAZARALOR, agility=False, intellect=True, strength=False, melee=False, ranged=False, source=Source.RAID, active=True
    ),
    Trinket(  # Dazar'Alor
        name="Variable Intensity Gigavolt Oscillating Reactor", item_id="165572", min_itemlevel=370, max_itemlevel=DAZARALOR+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=DAZARALOR, agility=True, intellect=False, strength=False, melee=False, ranged=False, source=Source.RAID, active=True
    ),
    Trinket(  # PvP
        name="Sinister Gladiator's Maledict", item_id="165806", min_itemlevel=370, max_itemlevel=M_PLUS_ITEMLEVEL+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=400, agility=True, intellect=True, strength=True, melee=False, ranged=False, source=Source.PVP, active=True
    ),
    Trinket(  # Crucible of Storms
        name="Lurker's Insidious Gift", item_id="167866", min_itemlevel=380, max_itemlevel=CRUCIBLE_OF_THE_STORMS+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=CRUCIBLE_OF_THE_STORMS, agility=True, intellect=False, strength=True, melee=False, ranged=False, source=Source.RAID, active=True
    ),
    Trinket(  # Crucible of Storms
        name="Harbinger's Inscrutable Will", item_id="167867", min_itemlevel=380, max_itemlevel=CRUCIBLE_OF_THE_STORMS+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=CRUCIBLE_OF_THE_STORMS, agility=False, intellect=True, strength=False, melee=False, ranged=False, source=Source.RAID, active=False
    ),
    Trinket(  # Profession
        name="Highborne Compendium of Sundering",
        item_id="169321",
        min_itemlevel=400,
        max_itemlevel=400,
        max_itemlevel_drop=400,
        agility=True,
        intellect=False,
        strength=True,
        melee=False,
        ranged=False,
        source=Source.PROFESSION,
        active=False
    ),
    Trinket(  # Profession
        name="Highborne Compendium of Storms",
        item_id="169328",
        min_itemlevel=400,
        max_itemlevel=400,
        max_itemlevel_drop=400,
        agility=False,
        intellect=True,
        strength=False,
        melee=False,
        ranged=False,
        source=Source.PROFESSION,
        active=False
    ),
    Trinket(  # World Boss
        name="Enthraller's Bindstone",
        item_id="169317",
        min_itemlevel=415,
        max_itemlevel=415+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=415,
        agility=True,
        intellect=True,
        strength=True,
        melee=False,
        ranged=False,
        source=Source.WORLD_BOSS,
        active=False
    ),
    Trinket(  # World Quest
        name="Oxidized Refuse Remover",
        item_id="170273",
        min_itemlevel=390,
        max_itemlevel=420+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=420,
        agility=True,
        intellect=True,
        strength=True,
        melee=False,
        ranged=False,
        source=Source.WORLD_QUEST,
        active=False
    ),
    Trinket(  # Eternal Palace
        name="Aquipotent Nautilus",
        item_id="169305",
        min_itemlevel=400,
        max_itemlevel=ETERNAL_PALACE+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=ETERNAL_PALACE,
        agility=False,
        intellect=True,
        strength=False,
        melee=False,
        ranged=False,
        source=Source.RAID,
        active=True
    ),
    Trinket(  # Eternal Palace
        name="Azshara's Font of Power",
        item_id="169314",
        min_itemlevel=400,
        max_itemlevel=ETERNAL_PALACE+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=ETERNAL_PALACE,
        agility=True,
        intellect=True,
        strength=True,
        melee=False,
        ranged=False,
        source=Source.RAID,
        active=True
    ),
    Trinket(  # Eternal Palace
        name="Leviathan's Lure",
        item_id="169304",
        min_itemlevel=400,
        max_itemlevel=ETERNAL_PALACE+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=ETERNAL_PALACE,
        agility=False,
        intellect=True,
        strength=False,
        melee=False,
        ranged=False,
        source=Source.RAID,
        active=False
    ),
    Trinket(  # Eternal Palace
        name="Shiver Venom Relic",
        item_id="168905",
        min_itemlevel=400,
        max_itemlevel=ETERNAL_PALACE+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=ETERNAL_PALACE,
        agility=False,
        intellect=True,
        strength=False,
        melee=False,
        ranged=False,
        source=Source.RAID,
        active=True
    ),
    Trinket(  # Eternal Palace
        name="Za'qul's Portal Key",
        item_id="169306",
        min_itemlevel=400,
        max_itemlevel=ETERNAL_PALACE+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=ETERNAL_PALACE,
        agility=False,
        intellect=True,
        strength=False,
        melee=False,
        ranged=False,
        source=Source.RAID,
        active=False
    ),
    Trinket(  # Eternal Palace
        name="Ashvane's Razor Coral",
        item_id="169311",
        min_itemlevel=400,
        max_itemlevel=ETERNAL_PALACE+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=ETERNAL_PALACE,
        agility=True,
        intellect=False,
        strength=True,
        melee=False,
        ranged=False,
        source=Source.RAID,
        active=True
    ),
    Trinket(  # Eternal Palace
        name="Dribbling Inkpod",
        item_id="169319",
        min_itemlevel=400,
        max_itemlevel=ETERNAL_PALACE+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=ETERNAL_PALACE,
        agility=True,
        intellect=False,
        strength=True,
        melee=False,
        ranged=False,
        source=Source.RAID,
        active=False
    ),
    Trinket(  # Eternal Palace
        name="Phial of the Arcane Tempest",
        item_id="169313",
        min_itemlevel=400,
        max_itemlevel=ETERNAL_PALACE+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=ETERNAL_PALACE,
        agility=True,
        intellect=False,
        strength=True,
        melee=False,
        ranged=False,
        source=Source.RAID,
        active=False
    ),
    Trinket(  # Eternal Palace
        name="Vision of Demise",
        item_id="169307",
        min_itemlevel=400,
        max_itemlevel=ETERNAL_PALACE+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=ETERNAL_PALACE,
        agility=True,
        intellect=False,
        strength=True,
        melee=False,
        ranged=False,
        source=Source.RAID,
        active=True
    ),
    Trinket(  # Mechagon
        name="Clockwork Re-Sharpener",
        item_id="161375",
        min_itemlevel=415,
        max_itemlevel=415+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=415,
        agility=True,
        intellect=False,
        strength=False,
        melee=False,
        ranged=False,
        source=Source.DUNGEON,
        active=True
    ),
    Trinket(  # World Boss
        name="Shockbiter's Fang",
        item_id="169318",
        min_itemlevel=415,
        max_itemlevel=415+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=415,
        agility=True,
        intellect=True,
        strength=True,
        melee=False,
        ranged=False,
        source=Source.WORLD_BOSS,
        active=True
    ),
    Trinket(  # Craftable
        name="Galvanic Turbo-Charger",
        item_id="161416",
        min_itemlevel=415,
        max_itemlevel=415,
        max_itemlevel_drop=415,
        agility=False,
        intellect=False,
        strength=True,
        melee=False,
        ranged=False,
        source=Source.PROFESSION,
        active=False
    ),
    Trinket(  # Profession
        name="Ascended Alchemist Stone",
        item_id="168676",
        min_itemlevel=440,
        max_itemlevel=450,
        max_itemlevel_drop=450,
        agility=True,
        intellect=True,
        strength=True,
        melee=False,
        ranged=False,
        source=Source.PROFESSION,
        active=False
    ),
    Trinket(  # Profession
        name="Ruthlessness Protocol Augment",
        item_id="161374",
        min_itemlevel=390,
        max_itemlevel=420+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=420,
        agility=False,
        intellect=True,
        strength=False,
        melee=False,
        ranged=False,
        source=Source.PROFESSION,
        active=False
    ),
    Trinket(  # Profession
        name="Self-Accelerating Drive Shaft",
        item_id="161414",
        min_itemlevel=390,
        max_itemlevel=420+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=420,
        agility=False,
        intellect=True,
        strength=False,
        melee=False,
        ranged=False,
        source=Source.PROFESSION,
        active=False
    ),
    Trinket(  # Worldquest
        name="Trunksy",
        item_id="155565",
        min_itemlevel=WORLD_QUEST_ITEMLEVEL,
        max_itemlevel=WORLD_QUEST_ITEMLEVEL+TITANFORGING_CUT_OFF,
        max_itemlevel_drop=WORLD_QUEST_ITEMLEVEL,
        agility=True,
        intellect=True,
        strength=True,
        melee=False,
        ranged=False,
        source=Source.WORLD_QUEST,
        active=False
    ),
    # Trinket(
    #     name="", item_id="", min_itemlevel=WORLD_QUEST_ITEMLEVEL, max_itemlevel=TITANFORGE_CAP,
    #     max_itemlevel_drop=TRADER_TOKEN, agility=False, intellect=False, strength=False, melee=False, ranged=False, active=False
    # ),
]
