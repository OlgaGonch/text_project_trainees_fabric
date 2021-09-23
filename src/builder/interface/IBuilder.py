from abc import ABC

from pandas import DataFrame


class IBuilder(ABC):
    ''' Выполнение команд по списку последовательно
      '''

    def register(self, command: ICommand) -> None:
        """Дополняет список comands к выполнению"""
        raise NotImplementedError()

    def execute(self, data: DataFrame) -> DataFrame:
        """Выполнение команд по списку"""
        raise NotImplementedError()
