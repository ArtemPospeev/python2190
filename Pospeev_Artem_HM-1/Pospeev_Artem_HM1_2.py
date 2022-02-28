cubes_lst, rslt_1, rslt_2 = [i**3 for i in range(1,1000,2)], 0, 0

for i in cubes_lst:
    number_for_circle = i  # переменная для изменения.
    sum_in_number = 0  # переменная для подсчета суммы цифр в числе.
    while (number_for_circle // 10 != 0):  # пока число делится нацело на 10
        sum_in_number += number_for_circle % 10  # запоминаем в переменную суммы остаток от деления
        number_for_circle //= 10  # изменяем число (оставляем только целую часть от деления)
    sum_in_number += number_for_circle  # добавляем остаток
    if sum_in_number % 7 == 0:
        rslt_1 += i

for i in cubes_lst:
    i += 17  # добавляем 17, не меняя изначальный список.
    number_for_circle = i
    sum_in_number = 0
    while (number_for_circle // 10 != 0):
        sum_in_number += number_for_circle % 10
        number_for_circle //= 10
    sum_in_number += number_for_circle
    if sum_in_number % 7 == 0:
        rslt_2 += i
print(rslt_1)
print(rslt_2)
