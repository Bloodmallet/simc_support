import enum


class Source(enum.Enum):
    UNKNOWN = "Unknown"
    TEMPLATE = "Template"

    CALLING = "Calling"
    DELVE = "Delve"  # 1-3 player dungeon
    DUNGEON = "Dungeon"
    MEGA_DUNGEON = "Mega Dungeon"
    """
    Another special kind of dungeon. Very long. Very tedious.
    Most likely will get split in into multiple m+ dungeons in the future.
    """
    MISSION = "Mission"
    PROFESSION = "Profession"
    PVP = "PvP"
    LOW_PVP = "Low PvP"
    HIGH_PVP = "High PvP"
    RAID = "Raid"
    RARE_MOB = "Rare Mob"
    TIMEWALKING = "Timewalking"
    WORLD_BOSS = "World Boss"
    WORLD_DROP = "World Drop"
    WORLD_QUEST = "World Quest"
