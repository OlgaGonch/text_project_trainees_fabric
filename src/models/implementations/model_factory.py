from ..interface.IFabric import AbstractFactory
from ..interface.IModel import IModel


class ModelFactory(AbstractFactory):
    def __init__(self):
        self._dictionary = {}

    def add_model(self,
                  model_type: str,
                  model_impl: IModel):
        if model_type not in self._dictionary:
            self._dictionary[model_type] = model_impl

    def get_instance(self,
                     name,
                     data_folder_path,
                     data_batches_path,
                     batch_size,
                     num_collection_passes,
                     count_of_terms
                     ) -> IModel:
        try:
            model_impl = self._dictionary[name]
        except KeyError:
            raise TypeError(f"Factory with type '{name}' not found.") from None
        else:
            return model_impl(data_folder_path, data_batches_path, batch_size, num_collection_passes, count_of_terms)


    '''def create_text_editor(self):
        return Stemmer()'''
