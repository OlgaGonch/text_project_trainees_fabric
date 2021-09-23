from abc import ABC
from copy import deepcopy
from typing import List

from pandas import DataFrame

from src.builder.interface.IBuilder import IBuilder

__all__ = [
    'BuilderImpl'
]


class BuilderImpl(IBuilder):
    ''' Выполнение команд по списку последовательно
      '''

    __slots__ = (
        '_data',
        '_commands'
    )

    def __init__(self):
        self._commands: List[ICommand] = []

    def register(self, command: ICommand) -> None:
        """Дополняет список comands к выполнению"""
        self._commands.append(command)
        print('ExecutorImp ', self._commands)
        return

    def execute(self, data: DataFrame) -> DataFrame:
        """Выполнение команд по списку"""
        _data = deepcopy(data)
        for command in self._commands:
            _data = command.execute(data=_data)
        return _data
