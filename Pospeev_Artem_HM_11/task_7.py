import cmath


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a  # a, b - вещественные числа, i - мнимая единица
        self.b = b
        self.i = cmath.sqrt(-1)

    def __str__(self):
        if self.b == 0:
            return f'{self.a}'
        else:
            return f'{self.a}' if self.b == 0 else f'{self.a + self.b * self.i}'

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.a + other.a, self.b + other.b)
        else:
            return ComplexNumber(self.a + other, self.b)

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)
        else:
            return ComplexNumber(self.a * other, self.b * other)


comp_numb_1 = ComplexNumber(3, 2)
comp_numb_2 = ComplexNumber(2, 5)
print(f'Первое комплексное число: {comp_numb_1}')
print(f'Второе комплексное число: {comp_numb_2}')
print(f'Сумма комплексных чисел: {comp_numb_1 + comp_numb_2}')
print(f'Первое комплексное число + 6 : {comp_numb_1 + 6}')
print(f'Произведение комплексных чисел: {comp_numb_1 * comp_numb_2}')
print(f'Первое комплексное число умноженное на 6 : {comp_numb_1 * 6}')
