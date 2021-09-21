import artm
import os
from typing import Any

from ..interface.ITextEditor import ITextEditor
from ..utils import stemming_text
from ...interface.IModel import IModel


class StemmingImpl(ITextEditor):
    def __init__(self):
        pass

    def execute(self,
                full_path: str
                ) -> None:

        with open(full_path) as f:
            lines = f.readlines()

        res = os.path.dirname(full_path) + '/text_with_stemming.txt'
        file = open(res, "wb")

        i = 0
        for line in lines:
            new_line = stemming_text(lines[8:])
            file.write((str(i) + ' |text ' + new_line + '\n').encode())
            i += 1

        file.close()

        return res







