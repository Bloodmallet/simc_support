class SimcObject(object):

    def __init__(self, full_name: str, simc_name: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.full_name = full_name
        self.simc_name = simc_name

    def __str__(self) -> str:
        return self.full_name

    def __repr__(self) -> str:
        return self.simc_name
