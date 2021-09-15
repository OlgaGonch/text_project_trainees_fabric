from abc import ABC

from abc import abstractmethod

from src.interface import IModel


class AbstractFactory(ABC):
    def add_model(self,
                  model_type: str,
                  model_impl: IModel):
        raise NotImplementedError()

    def get_instance(self,
                     name,
                     data_folder_path,
                     data_batches_path,
                     batch_size,
                     num_collection_passes,
                     count_of_terms
                     ) -> IModel:
        raise NotImplementedError()