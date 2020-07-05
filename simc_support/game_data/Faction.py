from simc_support.game_data.SimcObject import SimcObject


class Faction(SimcObject):
    """Factions divide the player base, usually have differences in
    storylines, and quests.
    """

    @property
    def name(self) -> str:
        """Return full name of the Faction.

        Returns:
            str: Name of the Faction
        """
        return self.full_name


ALLIANCE = Faction("Alliance", 'alliance')
HORDE = Faction("Horde", 'horde')

FACTIONS = (ALLIANCE, HORDE)
