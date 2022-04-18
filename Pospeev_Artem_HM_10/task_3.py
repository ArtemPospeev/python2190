# Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка».
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__floordiv__, __truediv__()).
# Эти методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и округление
# до целого числа деления клеток, соответственно.

class Cell:
    def __init__(self, start):
        self.cells_numb = start

    def __str__(self):
        return str(self.cells_numb)

    def __add__(self, other):
        if isinstance(other, Cell):
            return Cell(self.cells_numb + other.cells_numb)

    def __sub__(self, other):
        if isinstance(other, Cell) and (self.cells_numb >= other.cells_numb):
            return Cell(self.cells_numb - other.cells_numb)
        else:
            print('Value Error :)')

    def __mul__(self, other):
        if isinstance(other, Cell):
            return Cell(self.cells_numb * other.cells_numb)

    def __truediv__(self, other):
        if other.cells_numb != 0:
            return Cell(int(self.cells_numb / other.cells_numb))

    def __floordiv__(self, other):
        if other.cells_numb != 0:
            return Cell(self.cells_numb // other.cells_numb)

    def make_order(self, n_per_line):
        result_str = ''
        for i in range(1, self.cells_numb + 1):
            result_str += '*'
            if i % n_per_line == 0:
                result_str += '\n'
        return result_str


cell_1 = Cell(10)
cell_2 = Cell(300)
print(cell_2 + cell_1, cell_2 - cell_1, cell_2 * cell_1, cell_2 / cell_1, cell_2 // cell_1, sep='\n')
print(cell_1.make_order(4))


