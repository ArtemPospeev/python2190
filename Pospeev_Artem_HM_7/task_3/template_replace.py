# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача,
# которая решена, например, во фреймворке django.

from os import path, walk
from shutil import move

folder = path.abspath('my_project')
replace_object = 'templates'


def replace_dir(fold, repl_obj):
    for root, dirs, _ in walk(fold):
        if root.endswith(repl_obj):
            move(root, path.join(fold, repl_obj))


if __name__ == '__main__':
    replace_dir(folder, replace_object)
