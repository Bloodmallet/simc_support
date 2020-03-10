class SimcObject(object):
    """Base class to enforce the usage of full_name for the User and
    simc_names in the background for SimulationCraft.
    """

    def __init__(self, full_name: str, simc_name: str, *args, **kwargs):
        super().__init__()
        self.full_name = full_name
        self.simc_name = simc_name

    def __str__(self) -> str:
        return self.full_name

    def __repr__(self) -> str:
        return self.simc_name
