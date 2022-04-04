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
    for rslt in zip_longest(tut, klass[:len(tut)]):
        yield rslt


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Anton', 'Kirill'
]
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

# zipped_tutors = (i for i in zip_longest(tutors, klasses[:len(tutors)]))  #тот же генератор, только без yield


gen_with_klass_none = zipped_tutors(tutors, klasses)
print(f'Task 3:\nType: {type(gen_with_klass_none)}')
print(f'Полный вывод генератора, где список студентов больше списка классов (вернуть {None}):\n', *gen_with_klass_none)
# print(next(gen_with_klass_none)) # исключение StopIteration

gen_len_tutors = zipped_tutors(tutors[:-2], klasses)
print(f'\nПолный вывод генератора, где список студентов < числа классов (вернуть по количеству студентов):\n',
      *gen_len_tutors)
