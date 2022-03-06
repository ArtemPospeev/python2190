# Task 3
# Есть два списка
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
# Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние кортежи
# в виде: (<tutor>, None), например:
# ('Станислав', None)
# Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
# Подумать, в каких ситуациях генератор даст эффект.

from itertools import zip_longest


def zipped_tutors(tut, klass):
    for ind, rslt in enumerate(zip_longest(tut, klass, fillvalue=None)):
        if ind < len(tut):
            yield rslt
        else:
            break


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Anton', 'Kirill'
]
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

gen_with_klass_none = zipped_tutors(tutors, klasses)
print(f'Task 3:\nType: {type(gen_with_klass_none)}')
print(f'Полный вывод генератора, где список студентов больше списка классов (вернуть {None}):')
for i in gen_with_klass_none:
    print(i)
# print(next(gen_with_klass_none)) # исключение StopIteration
print(f'\nПолный вывод генератора, где список студентов < числа классов (вернуть по количеству студентов):')
gen_len_tutors = zipped_tutors(tutors[:-2], klasses)
for i in gen_len_tutors:
    print(i)
