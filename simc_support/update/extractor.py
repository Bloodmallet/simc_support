import abc
import typing

from update.utils import ArgsObject, LOCALE_TABLES, dbc


class Extractor(abc.ABC):
    def __init__(self, user_args: ArgsObject) -> None:
        self.user_args: ArgsObject = user_args

    @property
    @abc.abstractmethod
    def tables(self) -> typing.List[str]:
        ...

    @abc.abstractmethod
    def combine_into_json(self, data: typing.Dict[str, LOCALE_TABLES]) -> None:
        ...

    def extract(self) -> None:
        # convert db2 to json
        data = dbc(self.user_args, self.tables)

        self.combine_into_json(data)
