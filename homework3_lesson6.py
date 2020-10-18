"""
    3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker:
    def __init__(self):
        self.name = input("Имя сотрудника: ")
        self.surname = input("Фамилия сотрудника: ")
        self.position = input("Должность сотрудника: ")
        self._income = dict(wage=int(input("Введите оклад: ")),bonus=int(input("Введите премию: ")))

class Position(Worker):
    def get_full_name(self): return self.name + " " + self.surname

    def get_total_income(self): return self._income["wage"] + self._income["bonus"]

a = Position()
print(a.get_full_name())
print(a.get_total_income())
