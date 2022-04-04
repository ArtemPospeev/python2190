# * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
# Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе
# «руками» (не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.

from yaml import safe_load
import os

CODING = 'utf-8'


def rec_dirs(dct):
    for key, items in dct.items():  # Перебираем ключи-значения в словаре.
        if not os.path.exists(key):  # По ключам создаём директории и заходим в них
            os.mkdir(key)
        os.chdir(key)
        for item in items:
            if isinstance(item, dict):  # Если значение - словарь, то рекурсивно вызываем функцию
                rec_dirs(item)
            else:
                n_file = open(item, 'w', encoding=CODING)  # Если значение не словарь - создаём файл.
                n_file.close()
    os.chdir(r'../')  # Выходим на уровень выше после завершения работы функции


if __name__ == '__main__':
    with open('config.yaml', encoding=CODING) as f:
        structure = safe_load(f)
    rec_dirs(structure)
