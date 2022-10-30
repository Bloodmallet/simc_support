import enum


class Source(enum.Enum):
    UNKNOWN = "Unknown"
    TEMPLATE = "Template"

    CALLING = "Calling"
    DUNGEON = "Dungeon"
    MISSION = "Mission"
    PROFESSION = "Profession"
    PVP = "PvP"
    RAID = "Raid"
    RARE_MOB = "Rare Mob"
    WORLD_BOSS = "World Boss"
    WORLD_DROP = "World Drop"
    WORLD_QUEST = "World Quest"
