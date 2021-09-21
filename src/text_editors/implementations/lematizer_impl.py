import artm
from pandas import DataFrame
from typing import Any
import os
from ..interface.ITextEditor import ITextEditor
from ...interface.IModel import IModel
from src.text_editors.utils import lemmatize_text


class LemmatizerImpl(ITextEditor):
    def __init__(self):
        pass

    def execute(self,
                full_path: str
                ) -> None:
        with open(full_path) as f:
            lines = f.readlines()

        res = os.path.dirname(full_path) + '/text_lemmatized.txt'
        file = open(res, "wb")

        i = 0
        for line in lines:
            new_line = lemmatize_text(line[8:])
            file.write((str(i) + ' |text ' + new_line + '\n').encode())
            i += 1

        file.close()

        return res
