# Task 5
# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f'Task 5:\nИсходный список:\n{src}')
result = [i for i in src if src.count(i) == 1]
print(f'Список из уникальных элементов исходного списка (сохраняя их порядок):\n{result}')