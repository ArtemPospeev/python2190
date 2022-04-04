# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить
# конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет при
# этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

from os import makedirs, chdir


def create_sample():
    config_dct = {'--my_project': ['--settings', '--mainapp', '--adminapp', '--authapp']}
    for key, items in config_dct.items():
        makedirs(key, exist_ok=True)
        chdir(key)
        for item in items:
            makedirs(item, exist_ok=True)


if __name__ == '__main__':

    create_sample()
