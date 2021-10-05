import json
import os

import re
import string


def small_sample(
        path_to_initial_data: str,  # путь к исходному файлу
        path_to_data: str,  # файл для записи
) -> str:
    if not os.path.exists(os.path.dirname(path_to_data)):  # проверяем наличие папки для записи файлов
        print('Папки нет')
        os.mkdir(os.path.dirname(path_to_data))
    with open('{0}texts.txt'.format(path_to_initial_data), 'r', ) as txt_file, \
            open('{0}text_small_100.txt'.format(path_to_data), 'w+') as file_to_write:
        for i in range(100):
            x = txt_file.readline()
            file_to_write.write(x)
        return '{0}text_small_100.txt'.format(path_to_data)


def data_preparation(
        path_to_initial_data: str, # путь к исходному файлу
        path_to_data: str,
) -> None:

    remove = string.punctuation
    pattern = r"[{}]".format(remove)

    if not os.path.exists(os.path.dirname(path_to_data)):  # проверяем наличие папки для записи файлов
        print('Папки нет')
        os.mkdir(os.path.dirname(path_to_data))
    with open('{0}text_small_100.txt'.format(path_to_initial_data), 'r', ) as txt_file, \
            open('{0}text_ready.txt'.format(path_to_data), 'w+') as file_to_write:

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


if __name__ == "__main__":
    path_to_initial_data = os.path.abspath('../../data/') + '/'
    print(path_to_initial_data)
    path_to_data = os.path.abspath('../../data/tmp/') + '/'
    path_to_data = small_sample(path_to_initial_data, path_to_data)  # код для получения небольшой выборки
    # data_preparation(path_to_initial_data,
    #                  path_to_data)
