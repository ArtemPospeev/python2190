# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        return 'car going'

    def stop(self):
        return 'car stopped'

    def turn(self, direction):
        return f'car turned {direction}'

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self, speed_limit=60):
        if self.speed > speed_limit:
            print('over speed!', self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self, speed_limit=40):
        if self.speed > speed_limit:
            print('over speed!', self.speed)
        else:
            print(self.speed)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


p_car = PoliceCar(30, 'red', 'A344AV')
print(p_car.name, p_car.speed, p_car.is_police, p_car.color, p_car.is_police)
p_car.show_speed()
print(p_car.go(), p_car.turn('left'), p_car.stop(), sep='\n')

w_car = WorkCar(60, 'green', 'a545av')
print(w_car.name, w_car.speed, w_car.is_police, w_car.color, w_car.is_police)
w_car.show_speed()
w_car.speed = 40
w_car.show_speed()
