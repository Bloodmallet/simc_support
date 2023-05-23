import enum


class InstanceType(int, enum.Enum):
    UNKNOWN = -1
    DUNGEON = 1
    RAID = 2


class Instance(int, enum.Enum):
    NOT_MAPPED = -1

    # dungeons
    ALGETHAR_ACADEMY = 1201
    BRACKENHIDE_HOLLOW = 1196
    COURT_OF_STARS = 800
    HALLS_OF_INFUSION = 1204
    HALLS_OF_VALOR = 721
    NELTHARUS = 1199
    RUBY_LIFE_POOLS = 1202
    SHADOWMOON_BURIAL_GROUNDS = 537
    TEMPLE_OF_THE_JADE_SERPENT = 313
    THE_AZURE_VAULT = 1203
    THE_NOKHUD_OFFENSIVE = 1198
    ULDAMAN_LEGACY_OF_TYR = 1197

    FREEHOLD = 1001
    NELTHARIONS_LAIR = 767
    THE_UNDERROT = 1022
    VORTEX_PINNACLE = 68

    # Timewalking Cataclysm
    BLACKROCK_CAVERNS = 66
    END_TIME = 184
    LOST_CITY_OF_TOLVIR = 69
    THE_STONECORE = 67
    # THE_VORTEX_PINNACLE = 68
    THRONE_OF_THE_TIDES = 65

    # raids
    VAULT_OF_THE_INCARNATES = 1200
    ABERUS_THE_SHADOWED_CRUCIBLE = 1208
    FIRELANDS = 78


class RaidTier(int, enum.Enum):
    UNKNOWN = enum.auto()
    LOW = enum.auto()
    MID = enum.auto()
    HIGH = enum.auto()
    HIGHER = enum.auto()
    VERY_RARE = enum.auto()

    @staticmethod
    def get_raid_tier_from_encounter_id(encounter_id: int) -> "RaidTier":
        if encounter_id in (
            2480,  # Eranog
            2500,  # Terros
            2486,  # The Primal Council
            2482,  # Sennarth, the Cold Breath
            # Aberrus, the Shadowed Crucible
            2522,  # Kazzara, the Hellforged
            2529,  # The Amalgamation Chamber
            2524,  # Assault of the Zaqali
        ):
            return RaidTier.LOW
        elif encounter_id in (
            2502,  # Dathea, Ascended
            2491,  # Kurog Grimtotem
            # Aberrus, the Shadowed Crucible
            2530,  # The Forgotten Experiments
            2525,  # Rashok, the Elder
        ):
            return RaidTier.MID
        elif encounter_id in (
            2493,  # Broodkeeper Diurna
            2499,  # Raszageth the Storm-Eater
            # Abberus, the Shadowed Crucible
            2532,  # The Vigilant Steward, Zskarn
            2527,  # Magmorax
        ):
            return RaidTier.HIGH
        elif encounter_id in (
            2523,  # Echo of Neltharion
            2520,  # Scalecommander Sarkareth
        ):
            return RaidTier.HIGHER
        return RaidTier.UNKNOWN
