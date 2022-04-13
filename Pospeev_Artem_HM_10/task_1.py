# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |
#
# | 3 5 8 3 |
# | 8 3 7 1 |
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и пр.
from itertools import zip_longest


class Matrix:

    def __init__(self, lst):
        self.matr = lst

    def __str__(self):
        rslt = ''
        for matrs in self.matr:
            for matr in matrs:
                rslt += str(matr) + ' '
            rslt += '\n'
        return rslt

    def __iter__(self):
        self.i = -1  # счетчик для next и iter
        return self

    def __next__(self):
        self.i += 1
        if self.i < len(self.matr):
            return self.matr[self.i]
        else:
            raise StopIteration

    def __add__(self, other):
        summ_matrix = []
        for lst_one, lst_two in zip_longest(other, self.matr):
            if lst_one and lst_two and (len(lst_one) == len(lst_two)):
                summ_matrix.append([i + j for i, j in zip_longest(lst_one, lst_two)])
            else:
                return 'Матрицы должны быть одного размера'
        return Matrix(summ_matrix)


matr1 = Matrix([[31, 22],
                [37, 43],
                [51, -87]])
matr2 = Matrix([[1, 2],
                [1, 2],
                [1, 2]])
print(f'{matr1}\n{matr2}\n\n{matr1 + matr2}')
