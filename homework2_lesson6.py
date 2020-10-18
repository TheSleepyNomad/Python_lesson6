"""
    2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
    Например: 20м * 5000м * 25кг * 5см = 12500 т
"""
import argparse

parser = argparse.ArgumentParser(
    description="""Скрипт расчитывает массу асфальта, необходимую для покрытия дорожного полотна.
    Например: 20м * 5000м * 25кг * 5см = 12500 т""")

parser.add_argument('length', type=int, help='Длина дороги')
parser.add_argument('width', type=int, help='Ширина дороги')
parser.add_argument('asphalt_weight', type=int, help='Масса асфальта для покрытия 1м*2')
parser.add_argument('road_thickness', type=int, help='Толщина полотна')

args = parser.parse_args()


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_weight_calculate(self, asphalt_weight, road_thickness):
        return (self._length * self._width * asphalt_weight * road_thickness) // 1000


result = Road(args.length, args.width)
print(result.asphalt_weight_calculate(args.asphalt_weight, args.road_thickness),"т")