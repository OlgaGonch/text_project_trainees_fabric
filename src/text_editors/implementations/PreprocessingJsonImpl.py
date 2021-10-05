import json
import os
import re
import string
from typing import Any

from src.text_editors.interface.ITextEditor import ITextEditor


class PreprocessingJSONImpl(ITextEditor):
    def __init__(self):
        pass

    def execute(self, full_path: str) -> Any:
        path_to_data = os.path.abspath(os.path.dirname(full_path) + '/tmp/') + '/'

        if not os.path.exists(os.path.dirname(path_to_data)):  # проверяем наличие папки для записи файлов
            print('Папки нет')
            os.mkdir(os.path.dirname(path_to_data))
        with open(full_path, 'r', ) as txt_file, \
                open('{0}batch_of_text.txt'.format(os.path.dirname(full_path)), 'w+') as file_to_write:
            for i in range(10):
                x = txt_file.readline()
                file_to_write.write(x)

        #

        remove = string.punctuation
        pattern = r"[{}]".format(remove)

        if not os.path.exists(os.path.dirname(path_to_data)):  # проверяем наличие папки для записи файлов
            print('Папки нет')
            os.mkdir(os.path.dirname(path_to_data))
        with open('{0}batch_of_text.txt'.format(os.path.dirname(full_path)), 'r', ) as txt_file, \
                open('{0}batch_of_ready_text.txt'.format(path_to_data), 'w+') as file_to_write:

            string_number = 0  # счетчик слов для связи с исходным документом
            for x in txt_file:  # итерация по файлу
                x = x.replace(r'\\', '\\')  # замена для корректного чтения json
                data = json.loads(x)
                string_a = ''
                for i in data:
                    a = i['alternatives'][0]['transcript']  # текст разговора
                    a = re.sub(pattern, "", a)
                    if len(a) > 0:
                        string_a = string_a + a + ' '

                if len(string_a) > 50:  # пишем только разговоры с длиной от 50 символов
                    file_to_write.write(str(string_number) + ' |text ' + string_a + ',' + '\n')

                string_number += 1
        print('{0}batch_of_ready_text.txt'.format(path_to_data))
        return '{0}batch_of_ready_text.txt'.format(path_to_data)
