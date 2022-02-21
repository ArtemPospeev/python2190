cubes_lst, rslt = [], 0

for i in range(1, 1000, 2): # заполняем список нечетными числами от 1 до 1000
    cube = i ** 3
    cubes_lst.append(cube)

for i in cubes_lst:
    i += 17  # добавляем 17, не меняя изначальный список.
    number_for_circle = i  # переменная для изменения.
    sum_in_number = 0  # переменная для подсчета суммы цифр в числе.

    while (number_for_circle // 10 != 0):  # пока число делится нацело на 10
        sum_in_number += number_for_circle % 10  # запоминаем в переменную суммы остаток от деления
        number_for_circle //= 10  # изменяем число (оставляем только целую часть от деления)
    sum_in_number += number_for_circle  # добавляем остаток

    if sum_in_number % 7 == 0:
        rslt += i  # добавляем именно i, а не number_for_circle, т.к. то число изменялось

print(rslt)
