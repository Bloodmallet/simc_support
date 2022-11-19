import typing


def convert_to_simc_string(normal_string: str) -> str:
    """Converts a normal name into a simc_name.

    Args:
        normal_string (str): "My Awesome'st Name Ever"

    Returns:
        str: "my_awesomest_name_ever"
    """
    simc_name = normal_string.lower()
    cleansers = (
        (" ", "_"),
        ("-", ""),
        ("'", ""),
        (":", ""),
        (",", ""),
    )

    for cleanser in cleansers:
        simc_name = simc_name.replace(*cleanser)

    return simc_name


class SimcObject:
    """Base class to enforce the usage of full_name for the User and
    simc_names in the background for SimulationCraft.
    """

    def __init__(
        self, full_name: str, simc_name: typing.Optional[str] = None, *args, **kwargs
    ):
        super().__init__()
        self.full_name: str = full_name
        self._provided_simc_name: typing.Optional[str] = simc_name
        self._simc_name: str = ""

    @property
    def simc_name(self) -> str:
        if self._provided_simc_name:
            return self._provided_simc_name
        if self._simc_name:
            return self._simc_name

        self._simc_name = convert_to_simc_string(self.full_name)

        return self._simc_name

    def __str__(self) -> str:
        return self.full_name

    def __repr__(self) -> str:
        return self.simc_name
