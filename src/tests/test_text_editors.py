import os
import yaml

from dataclasses import dataclass
from typing import Any
from typing import Mapping
from unittest import TestCase

from src.builder.implementations.BuilderImpl import BuilderImpl
from src.models.implementations.model_factory import ModelFactory
from src.models.implementations.model_training import ModelTrainer
from src.text_editors.interface.ITextEditorFactory import TextEditorAbstractFactory
from src.text_editors.implementations.text_editor_factory import TextEditorFactory
from src.text_editors.implementations.lematizer_impl import LemmatizerImpl
from src.text_editors.implementations.stemming_impl import StemmingImpl
from src.models.interface.IModel import IModel


@dataclass
class RequestTDO:
    file_path: str


@dataclass
class SettingsTDO:
    preprocessing: str
    text_editor: str
    classification_model: IModel
    key_words: list
    settings: dict


def _get_settings_for_test(
        settings: Mapping[str, Any],
) -> SettingsTDO:
    _settings = SettingsTDO(**settings)
    return _settings


def _get_request_for_test(
        request: Mapping[str, Any],
) -> RequestTDO:
    _request = RequestTDO(**request)
    return _request


class TestDataPreparation(TestCase):  # подготовка данных из файла txt, где каждая строка - json файл

    def test_prepearing_init_data(self):
        # путь к данным
        data_path = os.path.abspath('../data/' + '/', )  # прописать путь к данным
        # файлы settings
        data_items = [
            {'file_path': '{0}/settings/data_lematizer_regs.yaml'.format(data_path)
             },
            {'file_path': '{0}/settings/data_lematizer_simple.yaml'.format(data_path)
             },
            {'file_path': '{0}/settings/data_stemming_regs.yaml'.format(data_path)
             },
            {'file_path': '{0}/settings/data_stemming_simple.yaml'.format(data_path)
             }
        ]
        # подготовка фабрики для выбора text_editor
        factory_preprocessing = TextEditorFactory()
        factory_preprocessing.add_text_editor('preprocessing', PreprocessingImpl())  # класс, который переводит текст из формата json в txt - не могу найти его в проекте
        factory_preprocessing.add_text_editor('lematizer', LemmatizerImpl())
        factory_preprocessing.add_text_editor('stemming', StemmingImpl())

        # подготовка фабрики для выбора модели BigartmSimple или BigartmRegs
        model_factory = ModelFactory()
        model_factory.add_model('BigARTMSimple', ModelTrainer)
        model_factory.add_model('BigARTMRegs', ModelTrainer)

        data_path = os.path.abspath('../data/' + '/', )  # прописать путь к данным
        data_items = [
            {'file_path': '{0}/settings/data_lematizer_regs.yaml'.format(data_path)
             },
            {'file_path': '{0}/settings/data_lematizer_simple.yaml'.format(data_path)
             },
            {'file_path': '{0}/settings/data_stemming_regs.yaml'.format(data_path)
             },
            {'file_path': '{0}/settings/data_stemming_simple.yaml'.format(data_path)
             }
        ]  # ссылка на файл

        for data_item in data_items:
            # вводим строитель
            text_convertor = BuilderImpl()

            data_request = _get_request_for_test(
                data_item)
            with open('{0}'.format(data_request.file_path), 'r') as stream:
                settings_dict = _get_settings_for_test(yaml.safe_load(stream))
            print(type(settings_dict.settings), settings_dict.settings)

            print('register')  # регистрируем команды в список Builder
            text_convertor.register(factory_preprocessing.get_instance(settings_dict.preprocessing))
            text_convertor.register(factory_preprocessing.get_instance(settings_dict.text_editor))

            print('execute ')
            df_text = pd.read_csv('{}/sentiment_analysis_train_numbers.csv'.format(data_path))
            full_text = pd.read_csv('{}/full_text.csv'.format(data_path))
            df_text = df_text[['number', 'call_text', 'estimate']]

            df_text_transformed = text_convertor.execute(df_text)
            full_text_transformed = text_convertor.execute(full_text)

            SklearnModelsent = SklearnModelImpl()
            train_text, train_labels, test_text, test_labels = SklearnModelsent.split_into_training_and_test(
                0.1,
                df_text_transformed)

            preprocessing_product = factory_preprocessing.get_instance(settings_dict.text_editor)
            print(preprocessing_product)
            texts_df = preprocessing_product.execute(full_path='{0}{1}'.format(data_path,
                                                                               settings_dict.settings.get('data_folder_path')))
        result = True
        self.assertTrue(result, 'good')