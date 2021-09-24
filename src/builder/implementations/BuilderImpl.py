from abc import ABC
from copy import deepcopy
from typing import List

from pandas import DataFrame

from src.builder.interface.IBuilder import IBuilder
from ...text_editors.interface.ITextEditor import ITextEditor

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
        self._commands: List[ITextEditor] = []

    def register(self, command: ITextEditor) -> None:
        """Дополняет список comands к выполнению"""
        self._commands.append(command)
        print('ExecutorImp ', self._commands)
        return

    def execute(self, full_path: str) -> str:
        """Выполнение команд по списку"""
        for command in self._commands:
            res_path: str = command.execute(full_path=full_path)
        return res_path
