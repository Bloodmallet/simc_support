import enum


class InstanceType(int, enum.Enum):
    UNKNOWN = -1
    DUNGEON = 1
    RAID = 2


class Instance(int, enum.Enum):
    NOT_MAPPED = -1

    # dungeons
    ALGETHAR_ACADEMY = 1201
    COURT_OF_STARS = 800
    HALLS_OF_VALOR = 721
    NELTHARUS = 1199
    RUBY_LIFE_POOLS = 1202
    SHADOWMOON_BURIAL_GROUNDS = 537
    TEMPLE_OF_THE_JADE_SERPENT = 313
    THE_AZURE_VAULT = 1203
    THE_NOKHUD_OFFENSIVE = 1198

    # raids
    VAULT_OF_THE_INCARNATES = 1200


class RaidTier(int, enum.Enum):
    UNKNOWN = enum.auto()
    LOW = enum.auto()
    MID = enum.auto()
    HIGH = enum.auto()

    @staticmethod
    def get_raid_tier_from_encounter_id(encounter_id: int) -> "RaidTier":
        if encounter_id in (
            2480,  # Eranog
            2500,  # Terros
            2486,  # The Primal Council
            2482,  # Sennarth, the Cold Breath
        ):
            return RaidTier.LOW
        elif encounter_id in (
            2502,  # Dathea, Ascended
            2491,  # Kurog Grimtotem
        ):
            return RaidTier.MID
        elif encounter_id in (
            2493,  # Broodkeeper Diurna
            2499,  # Raszageth the Storm-Eater
        ):
            return RaidTier.HIGH
        return RaidTier.UNKNOWN
