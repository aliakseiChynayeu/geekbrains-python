# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и
# премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В
# классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (
# get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    _name: str
    _surname: str
    _position: str
    _income = {"wage": 0., "bonus": 0.}

    def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float):
        self._name = name
        self._surname = surname
        self._position = position
        self._income["wage"] = wage
        self._income["bonus"] = bonus


class Position(Worker):

    def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float):
        super().__init__(name, surname, position, wage, bonus)

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")

    def get_full_name(self):
        return f"{self._name} {self._surname}"


position = Position("Jhon", "Doh", "developer", 100, 50)

print(f"{position.get_full_name()} total income : {position.get_total_income()}")
