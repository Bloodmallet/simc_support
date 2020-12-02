import typing

class SimcObject(object):
    """Base class to enforce the usage of full_name for the User and
    simc_names in the background for SimulationCraft.
    """

    def __init__(self, full_name: str, simc_name: typing.Optional[str] = None, *args, **kwargs):
        super().__init__()
        self.full_name = full_name
        self._simc_name = simc_name

    @property
    def simc_name(self) -> str:
        if self._simc_name:
            return self._simc_name

        simc_name = self.full_name.lower()
        cleansers = (
            (" ", "_"),
            ("-", ""),
            ("'", ""),
            (":", ""),
            (",", ""),
        )

        for cleanser in cleansers:
            simc_name = simc_name.replace(*cleanser)

        self._simc_name = simc_name

        return self._simc_name

    def __str__(self) -> str:
        return self.full_name

    def __repr__(self) -> str:
        return self.simc_name
