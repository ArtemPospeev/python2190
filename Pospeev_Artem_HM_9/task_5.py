# Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса
# метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручки')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандаша')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркера')


handle = Handle('A11s')
print(handle.title)
handle.draw()

pencil = Pencil('A22s')
print(pencil.title)
pencil.draw()

pen = Pen('A33s')
print(pen.title)
pen.draw()

pen_st = Stationery('pen A44s')
print(pen_st.title)
pen_st.draw()
