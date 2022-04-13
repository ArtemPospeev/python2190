#  Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
#  — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм.
#  У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
#  V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
#  для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
#  Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size, number=None):
        self.size = abs(size)
        self.serial_number = number

    @abstractmethod
    def flow_calc(self):
        pass

    def __str__(self):
        return f'{self.flow_calc} m^2'


class Coat(Clothes):

    @property
    def flow_calc(self):
        return round(self.size / 6.5 + 0.5, 2)

    def __add__(self, other):
        return Coat(self.size + other.size)


class Costume(Clothes):

    @property
    def flow_calc(self):
        return self.size * 2 + 0.3

    def __add__(self, other):
        return Costume(self.size + other.size)


costume_1 = Costume(20, 100)
costume_2 = Costume(25, 101)
coat_1 = Coat(170, 1000)
coat_2 = Coat(167, 1001)

for i in (costume_1, costume_2, coat_1, coat_2):
    print(f'Для пошива изделия № {i.serial_number} потребуется - {i} ткани')

print(f'Всего ткани на пошив 4 изделий - {costume_1 + costume_2 + coat_1 + coat_2}')
