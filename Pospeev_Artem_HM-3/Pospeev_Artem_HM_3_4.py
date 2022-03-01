# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия»
# и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные
# по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы

def thesaurus(name_lst):
    rslt_dct = {}

    for name in name_lst:

        if name[0] not in rslt_dct:
            rslt_dct[name[0]] = []
        rslt_dct[name[0]].append(name)

    return rslt_dct


def thesaurus_adv(*args):
    user_data_list, rslt_dct = list(map(str, args)), {}

    for full_name in user_data_list:  # перебираем список с фио
        full_name = full_name.title()  # проявляем лояльность к входящим данным
        name, surname = full_name.split(' ')  # берем фамилию
        if surname[0] not in rslt_dct:  # если в словаре нет ключа по первой букве фамилии - создаём
            rslt_dct[surname[0]] = []
        rslt_dct[surname[0]].append(full_name)

    for key, item in rslt_dct.items():  # перебираем полученный словарь, на место значений подставляем словари по именам
        rslt_dct[key] = thesaurus(item)  # функция уже была написана под прошлое задание, просто немного доработал

    return rslt_dct


dct_before_sorting = thesaurus_adv("Иван вИтюкин", "Игорь Бабушкин", "Инна Андреева", "Петр Ванюткин", "Илья Баваров")
print(f'Словарь до сортировки:\n{dct_before_sorting}', end='\n\n')

dct_after_sorting = dict(sorted(dct_before_sorting.items(), key=lambda x: x[0]))
print(f'Словарь после сортировки:\n{dct_after_sorting}')
