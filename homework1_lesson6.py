"""
    1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
— на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
    Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
и завершать скрипт.
"""
from time import sleep

# Инициализируем класс сфетофор
class TrafficLight:
    __color = "Red" # Артибут color будет иметь по умолчанию красный цвет

    def running(self):
        # Если цвет сменят через _TrafficLight__color, то метод running прекратит работу
        if self.__color != "Red":
            return "Red color is first. def running - stop!"
        print(self.__color)
        sleep(7)
        self.__color = "Yellow"
        print(self.__color)
        sleep(2)
        self.__color = "Green"
        print(self.__color)
        sleep(5)


# Создаем объект
traff_light = TrafficLight()
# Проверяем работу метода running
print(traff_light.running())
# Проверяем проверку на порядок режимов
traff_light._TrafficLight__color = "Yellow"
print(traff_light.running())

