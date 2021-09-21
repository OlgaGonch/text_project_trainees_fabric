from re import T
from typing import Any
from typing import BinaryIO, Type
from pandas import DataFrame

__all__ = [
    "ITextEditor",
]


class ITextEditor:

    def execute(self,
                full_path: str
                ) -> Any:
        raise NotImplementedError()
