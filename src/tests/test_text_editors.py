import os
import yaml

from dataclasses import dataclass
from typing import Any
from typing import Mapping
from unittest import TestCase

from src.builder.implementations.BuilderImpl import BuilderImpl
from src.models.implementations.ModelFactory import ModelFactory
from src.models.implementations.ModelTraining import ModelTrainer
from src.text_editors.implementations.PreprocessingJsonImpl import PreprocessingJSONImpl
from src.text_editors.implementations.TextEditorFactory import TextEditorFactory
from src.text_editors.implementations.LemmatizerImpl import LemmatizerImpl
from src.text_editors.implementations.StemmingImpl import StemmingImpl
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
        factory_preprocessing.add_text_editor('preprocessing', PreprocessingJSONImpl())
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
            text_convertor = BuilderImpl()  # строитель предобработки текста

            data_request = _get_request_for_test(
                data_item)
            with open('{0}'.format(data_request.file_path), 'r') as stream:
                settings_dict = _get_settings_for_test(yaml.safe_load(stream))

            print('register')  # регистрируем команды в список Builder
            text_convertor.register(factory_preprocessing.get_instance(settings_dict.preprocessing))
            text_convertor.register(factory_preprocessing.get_instance(settings_dict.text_editor))

            print('execute ')  # выполнение команд из списка
            res_path = text_convertor.execute(full_path='{0}{1}'.format(data_path, settings_dict.settings.get('data_folder_path')))
            print(res_path)

            # выбор модели BigARTM и передача в нее настроек
            BigARTMmodel = model_factory.get_instance(name=settings_dict.classification_model,
                                                      data_folder_path=res_path,
                                                      data_batches_path='{0}{1}'.format(data_path,settings_dict.settings.get('data_batches_path')),
                                                      batch_size=settings_dict.settings.get('batch_size'),
                                                      num_collection_passes=settings_dict.settings.get('num_collection_passes'),
                                                      count_of_terms=settings_dict.settings.get('count_of_terms'))
            model_artm_fitted = BigARTMmodel.train_model()
            print(model_artm_fitted)


        result = True
        self.assertTrue(result, 'good')