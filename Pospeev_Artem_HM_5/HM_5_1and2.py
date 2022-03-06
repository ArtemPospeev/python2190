# Task 1
# # Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield
# #
# # Task 2*
# # (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield


def odd_nums(num):
    for j in range(1, num + 1, 2):
        yield j


n = 15
odd_nums_def_n = odd_nums(n)
print(f'Task 1:\nType: {type(odd_nums_def_n)}')
print(f'Полный вывод генератора с yield:')
for i in odd_nums_def_n:
    print(i, end=' ')

# print(next(odd_nums_def_n))  # исключение stop iteration


odd_nums_2 = (i for i in range(1, n + 1, 2))
print(f'\n\nTask 2:\nType: {type(odd_nums_2)}')
print(f'Полный вывод генератора без yield:')
for i in odd_nums_2:
    print(i, end=' ')

# print(next(odd_nums_2))  # исключение stop iteration
