from abc import ABC

from pandas import DataFrame

from ...text_editors.interface.ITextEditor import ITextEditor


class IBuilder(ABC):
    ''' Выполнение команд по списку последовательно
      '''

    def register(self, command: ITextEditor) -> None:
        """Дополняет список comands к выполнению"""
        raise NotImplementedError()

    def execute(self, full_path: str) -> DataFrame:
        """Выполнение команд по списку"""
        raise NotImplementedError()
