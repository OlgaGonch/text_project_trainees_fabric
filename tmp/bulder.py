from abc import ABC, abstractmethod
from enum import Enum, auto
from collections import namedtuple

ProductBase = namedtuple('TextEditorType', 'ModelType')  # не поняла, для чего используется


class TextEditorType(Enum):
    STEMMER = auto()
    LEMMATIZER = auto()


class ModelType(Enum):
    BIGARTMSIMLE = auto()
    BIGARTMREG = auto()


class Product:  # где интерфейс?
    def __init__(self, name):
        self.name = name
        self.text_editor_type = None
        self.model_type = None

    def __str__(self):
        info: str = f"Product name: {self.name} \n" \
                    f"Text Editor type: {self.text_editor_type} \n" \
                    f"Model type: {self.model_type} \n"
        return info


class Builder(ABC): # отлично! но реализация классов  BigARTMSimpleWithStemming и BigARTMSimpleWithLemmatization не совсем правильная

    @abstractmethod
    def add_text_editor(self) -> None: pass

    @abstractmethod
    def add_model(self) -> None: pass

    @abstractmethod
    def get_product(self) -> Product: pass


class BigARTMSimpleWithStemming(Builder): #  класс получился немасштабируемым, лучше передавать параметры, а не прописывать все в методах

    def __init__(self):
        self.product = Product("BigARTMSimpleWithStemming")

    def add_text_editor(self) -> None: # я бы тоже сделала фабрику: выбор LEMMATIZER или STEMMER, и передачу параметров: add_text_editor(self, text_editor_type)
        self.product.text_editor_type = TextEditorType.LEMMATIZER

    def add_model(self) -> None:  # нужно сделать вызов с использованием фабрики и передачей типа модели в параметрах
        self.product.model_type = ModelType.BIGARTMSIMLE

    def get_product(self) -> Product: # ок
        return self.product


class BigARTMSimpleWithLemmatization(Builder): # см. замечания в BigARTMSimpleWithStemming

    def __init__(self):
        self.product = Product("BigARTMSimpleWithLemmatization")

    def add_text_editor(self) -> None:
        self.product.text_editor_type = TextEditorType.LEMMATIZER

    def add_model(self) -> None:
        self.product.model_type = ModelType.BIGARTMSIMLE

    def get_product(self) -> Product:
        return self.product


class Director: # если BigARTMSimpleWithLemmatization и BigARTMSimpleWithStemmin объединить с использованием 2х фабрик, то можно удалить директора, но так тоже можно
    def __init__(self):
        self.builder = None

    def set_builder(self, builder: Builder):
        self.builder = builder

    def make_product(self):
        if not self.builder:
            raise ValueError("Builder didn't set")
        self.builder.add_text_editor()
        self.builder.add_model()


if __name__ == '__main__':
    director = Director()
    for p in (BigARTMSimpleWithStemming, BigARTMSimpleWithLemmatization):
        builder = p()
        director.set_builder(builder)
        director.make_product()
        product = builder.get_product()
        print(product)
        print('-------------------------------------')
