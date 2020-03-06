""" Lib to check simc_options input values
"""
from typing import Union


class FightStyle(object):
    """Collection of all fight style related information
    """

    PATCHWERK = "patchwerk"
    LIGHTMOVEMENT = "lightmovement"
    HEAVYMOVEMENT = "heavymovement"
    HECTICADDCLEAVE = "hecticaddcleave"
    BEASTLORD = "beastlord"
    HELTERSKELTER = "helterskelter"
    DUNGEONSLICE = "dungeonslice"

    def get_fight_styles(self) -> tuple:
        """Returns a touple of all fight styles

        Returns:
        touple -- Containing all fight styles
        """

        return (
            self.PATCHWERK,
            self.LIGHTMOVEMENT,
            self.HEAVYMOVEMENT,
            self.HECTICADDCLEAVE,
            self.BEASTLORD,
            self.HELTERSKELTER,
            self.DUNGEONSLICE,
        )

    def is_fight_style(self, fight_style: Union[str, list]) -> bool:
        """Returns true if fight_style is known and spelled correctly.

        Arguments:
        fight_style {str,list} -- [description]

        Returns:
        bool -- Known and spelled correctly fight style/-s
        """

        # downwards compatibility
        if type(fight_style) == list:
            return self.is_fight_style_list(fight_style)
        fight_style_list = self.get_fight_styles()
        if not fight_style in fight_style_list:
            return False
        return True

    def is_fight_style_list(self, fight_styles: list) -> bool:
        """Returns true if all fight styles are spelled correctly and are known.

        Arguments:
        fight_styles {list} -- [description]

        Returns:
        bool -- [description]
        """

        fight_style_list = self.get_fight_styles()
        for fight_style in fight_styles:
            if not type(fight_style) == str:
                return False
            if not fight_style in fight_style_list:
                return False
        return True


class Tier(object):
    PR = "PR"
    T21 = "T21"
    T22 = "T22"
    T23 = "T23"
    T24 = "T24"

    def get_tiers(self) -> tuple:
        """Return a tuple of all known tiers.

        Returns:
        tuple -- [description]
        """

        return (
            self.PR,
            self.T21,
            self.T22,
            self.T23,
            self.T24,
        )

    def is_tier(self, tier: str) -> bool:
        """Returns true if tier is known.

        Arguments:
        profile {str} -- [description]

        Returns:
        bool -- [description]
        """

        for base_profile in self.get_tiers():
            if tier == base_profile:
                return True
        return False
