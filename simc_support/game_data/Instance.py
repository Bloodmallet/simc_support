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

    # Dragonflight S2
    FREEHOLD = 1001
    NELTHARIONS_LAIR = 767
    THE_UNDERROT = 1022
    VORTEX_PINNACLE = 68

    # Dragonflight S3
    # DAWN_OF_THE_INFINITE_GALAKRONDS_FALL = 1209
    # DAWN_OF_THE_INFINITE_MUROZOND_RISE = 1209
    DARKHEART_THICKET = 762
    BLACK_ROOCK_HOLD = 740
    WAYCREST_MANOR = 1021
    ATAL_DAZAR = 968
    EVERBLOOM_MPLUS = 556
    # THRONE_OF_THE_TIDES_MPLUS = 65

    # Timewalking Cataclysm
    BLACKROCK_CAVERNS = 66
    END_TIME = 184
    LOST_CITY_OF_TOLVIR = 69
    THE_STONECORE = 67
    # THE_VORTEX_PINNACLE = 68
    THRONE_OF_THE_TIDES = 65

    DAWN_OF_THE_INFINITE = 1209

    # raids
    VAULT_OF_THE_INCARNATES = 1200
    ABERUS_THE_SHADOWED_CRUCIBLE = 1208
    FIRELANDS = 78
    AMIRDRASSIL_THE_DREAMS_HOPE = 1207


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
            # Amirdrassil, the Dream's Hope
            2564,  # Gnarlroot
            2554,  # Igira the Cruel
        ):
            return RaidTier.LOW
        elif encounter_id in (
            2502,  # Dathea, Ascended
            2491,  # Kurog Grimtotem
            # Aberrus, the Shadowed Crucible
            2530,  # The Forgotten Experiments
            2525,  # Rashok, the Elder
            # Amirdrassil, the Dream's Hope
            2557,  # Volcoross
            2555,  # Council of Dreams
        ):
            return RaidTier.MID
        elif encounter_id in (
            2493,  # Broodkeeper Diurna
            2499,  # Raszageth the Storm-Eater
            # Abberus, the Shadowed Crucible
            2532,  # The Vigilant Steward, Zskarn
            2527,  # Magmorax
            # Amirdrassil, the Dream's Hope
            2553,  # Larodar, Keeper of the Flame
            2556,  # Nymue, Weaver of the Cycle
            2563,  # Smolderon
        ):
            return RaidTier.HIGH
        elif encounter_id in (
            # Abberus, the Shadowed Crucible
            2523,  # Echo of Neltharion
            2520,  # Scalecommander Sarkareth
            # Amirdrassil, the Dream's Hope
            2565,  # Tindral Sageswift, Seer of Flame
            2519,  # Fyrakk the Blazing
        ):
            return RaidTier.HIGHER
        return RaidTier.UNKNOWN
