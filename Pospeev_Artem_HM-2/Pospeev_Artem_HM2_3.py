# Решить задачу 2 не создавая новый список (как говорят, in place).
# Эта задача намного серьёзнее, чем может сначала показаться.


default_lst, i = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов'], 1

for word in default_lst[1:-1]:  # срез списка со второго до предпоследнего элемента
    str_stash = ''
    if word.isnumeric():  # если слово из списка принадлежит "числу"
        if 0 < int(word) <= 9:  # добавляем "0", если число состоит из 1 цифры
            word = '0' + word
            default_lst[i] = word
        default_lst.insert(i, '"')  # добавляем ковычки ПЕРЕД числом
        i += 1

    elif word[0] in ['+', '-', '/', '*'] and word[1].isnumeric():
        str_stash += word[0]  # записываем первый символ в строку
        if 0 < int(word[1:]) <= 9:
            str_stash += '0' + word[1:]  # добавляем "0" и остальную часть строки (число)
        else:
            str_stash += word[1:]  # в противном случае добавляем просто число
        default_lst[i] = str_stash
        default_lst.insert(i, '"')  # добавляем ковычки ПЕРЕД числом
        i += 1

    i += 1

i = -1  # т.к. теперь будем итерировать в обратном направлении

for word in default_lst[-2:1:-1]:  # берем срез с предпоследнего до второго элемента списка (перебираем реверсивно)
    str_stash = ''
    if word.isnumeric():
        default_lst.insert(i, '"')
        i -= 1  # отнимаем счетчик, т.к. идёт сдвиг из-за ковычки

    elif word[0] in ['+', '-', '/', '*'] and word[1].isnumeric():  # аналог с действием выше, но без "0"
        str_stash += word[0]
        str_stash += word[1:]
        default_lst[i - 1] = str_stash
        default_lst.insert(i, '"')
        i -= 1
    i -= 1

if default_lst[0].isnumeric():  # проверка первого элемента на "число"
    if 0 < int(default_lst[0]) <= 9:
        default_lst[0] = '0' + default_lst[0]
    default_lst.insert(1, '"')
    default_lst.insert(0, '"')

if default_lst[0][0] in ['+', '-', '/', '*'] and default_lst[0][1].isnumeric():  # проверка первого элемента на +"число"
    default_lst[0] = default_lst[0][0] + '0' + default_lst[0][1:]
    default_lst.insert(1, '"')
    default_lst.insert(0, '"')

if default_lst[-1].isnumeric():  # проверка последнего элемента на "число"
    if 0 < int(default_lst[-1]) <= 9:
        default_lst[-1] = '0' + default_lst[-1]
    default_lst.insert(-1, '"')
    default_lst.append('"')

if default_lst[-1][0] in ['+', '-', '/', '*'] and default_lst[-1][1].isnumeric():  # последний на + "число"
    default_lst[-1] = default_lst[-1][0] + '0' + default_lst[-1][1:]
    ind = len(default_lst)
    default_lst.insert(ind, '"')
    default_lst.insert(-2, '"')

print(f'Вывод обработанной строки (обратка без создания второго списка):\n{" ".join(default_lst)}')
