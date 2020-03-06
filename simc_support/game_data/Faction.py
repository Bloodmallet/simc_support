class Faction(object):
    """Factions divide the player base, usually have differences in storylines,
    and quests.
    """

    def __init__(self, full_name: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.full_name = str(full_name)

    def __repr__(self) -> str:
        return self.full_name

    def __str__(self) -> str:
        return self.full_name

    @property
    def name(self) -> str:
        """Return full name of the Faction.

        Returns:
            str: Name of the Faction
        """
        return self.full_name


ALLIANCE = Faction("Alliance")
HORDE = Faction("Horde")

FACTIONS = [ALLIANCE, HORDE]
