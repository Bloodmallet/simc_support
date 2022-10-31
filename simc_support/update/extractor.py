import abc
import typing

from simc_support.update.utils import ArgsObject, LOCALE_TABLES, dbc


class Extractor(abc.ABC):
    """Abstract class. The following must be implemented

    Properties:
        - tables

    Methods:
        - combine_into_json

    Execution entry point is `.extract()`

    """

    def __init__(self, user_args: ArgsObject) -> None:
        self.user_args: ArgsObject = user_args

    @property
    @abc.abstractmethod
    def tables(self) -> typing.List[str]:
        """List of all wow tables required for this Extractor.

        Returns:
            typing.List[str]: wow table names
        """
        ...

    @abc.abstractmethod
    def combine_into_json(self, data: typing.Dict[str, LOCALE_TABLES]) -> None:
        """Actions required to extract data from tables. Writes result to a single file.

        Args:
            data (typing.Dict[str, LOCALE_TABLES]): _description_
        """
        ...

    def extract(self) -> None:
        """Extract data and save it to file."""
        # convert db2 to json
        data = dbc(self.user_args, self.tables)

        self.combine_into_json(data)
