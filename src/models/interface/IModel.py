from re import T
from typing import Any
from typing import BinaryIO, Type

__all__ = [
    "IModel",
]

class IModel:

    # @classmethod
    """def load(cls: Type[T], stream: BinaryIO) -> T:
                Загружает модель из бинарного потока.
        
        raise NotImplementedError()

    def dump(self, stream: str) -> None:
        
        Сохраняет модель в файл.
        
        raise NotImplementedError()
        """

    def train_model(self
                    ) -> Any:
        """
        Обучает модель с нуля.

        :initial_data : исходные тексты
        :calls_data : батчи
        :return:
        """
        raise NotImplementedError()