"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево)
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""


class Car:
    def __init__(self):
        self.speed = int(input("Укажите скорость: "))
        self.color = input("Укажите цвет: ")
        self.name = input("Укажите модель: ")
        self.is_police = False
        if self.speed > 0:
            self.go()
        self.show_speed()

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина останавилась")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        print(f"Текущая скорость автомабиля {self.speed}км/ч")


class TownCar(Car):
    def __init__(self):
        print('Это городская машина. Максимальная допустимая скорость - 60км')
        super().__init__()
        if self.speed > 60:
            while self.speed > 60:
                self.speed = int(input("Уменьшите скорость авто: "))
    def show_speed(self):
        if self.speed > 60:
            print("!!!Превышение скорости!!!\nМаксимальная возможная скорость - 60км/ч")


class SportCar(Car):
    pass


class WorkCar(Car):
    def __init__(self):
        print('Это рабочая машина. Максимальная допустимая скорость - 40км')
        super().__init__()
        if self.speed > 40:
            while self.speed > 40:
                self.speed = int(input("Уменьшите скорость авто: "))
    def show_speed(self):
        if self.speed > 40:
            print("!!!Превышение скорости!!!\nМаксимальная возможная скорость - 40км/ч")


class PoliceCar(Car):
    def __init__(self):
        print('Это полицейская машина. Максимальная допустимая скорость - 40км')
        super().__init__()
        self.is_police = True

# Создаем объект на основании базового класса Car
just_car = Car()
# Проверяем методы
just_car.go()
just_car.stop()
just_car.turn("left")
# Создаем объект на основании класса TownCar и WorkCar для проверки сообщения о превышении скорости
town_car = TownCar()
work_car = WorkCar()
print(work_car.is_police)
# Создаем объект на основании класса PoliceCar и проверяем переопределенный атрибут is_police
police_car = PoliceCar()
print(police_car.is_police)
