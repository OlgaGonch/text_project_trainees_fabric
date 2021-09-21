from abc import ABC

from src.text_editors.interface import ITextEditor


class TextEditorAbstractFactory(ABC):
    def add_text_editor(self,
                  model_type: str,
                  model_impl: ITextEditor):
        raise NotImplementedError()

    def get_instance(self, name) -> ITextEditor:
        raise NotImplementedError()
