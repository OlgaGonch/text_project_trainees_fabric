from src.text_editors.interface import ITextEditor
from src.text_editors.interface.ITextEditorFactory import TextEditorAbstractFactory


class TextEditorFactory(TextEditorAbstractFactory):
    def __init__(self):
        self._dictionary = {}

    def add_text_editor(self,
                  model_type: str,
                  model_impl: ITextEditor):
        if model_type not in self._dictionary:
            self._dictionary[model_type] = model_impl

    def get_instance(self, name) -> ITextEditor:
        try:
            model_impl = self._dictionary[name]
        except KeyError:
            raise TypeError(f"Factory with type '{name}' not found.") from None
        else:
            return model_impl


    '''def create_text_editor(self):
        return Stemmer()'''
