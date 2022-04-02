# Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же,
# а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
#   {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.

from os import walk
from os.path import join, getsize, splitext
from json import dump

folder = r'C:\Users\pospe\Desktop\PyProject'
result_dct = {}


def return_key(size_f):
    if size_f < 10:
        result = 0
    else:
        result = int('1' + '0' * (len(str(size_f)) - 1))
    return result


for roots, _, files in walk(folder):
    for file in files:
        file_size = getsize(join(roots, file))
        file_ext = splitext(file)[1]
        key = return_key(file_size)
        if key in result_dct:
            result_dct[key].append((file_size, file_ext))
        else:
            result_dct[key] = [(file_size, file_ext)]  # Ключ- 0, 10.. Значение- [(размер файла, расширение файла), ...]

for key, items in result_dct.items():  # Ключи те же, значения- (количество файлов, [расширения файлов])
    ext_set = set()
    for item in items:
        ext_set.add(item[1])
    result_dct[key] = (len(items), list(ext_set))

with open('summary.json', 'w+', encoding='utf-8') as f:
    dump(result_dct, f)
