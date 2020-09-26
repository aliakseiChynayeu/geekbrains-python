# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
# (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

class Stationery:
    _title: str

    def draw(self):
        print("Start drawing")


class Pen(Stationery):

    def __init__(self):
        self._title = "Pen"

    def draw(self):
        print("Start drawing with Pen")


class Pencil(Stationery):

    def __init__(self):
        self._title = "Pencil"

    def draw(self):
        print("Start drawing with Pencil")


class Handle(Stationery):

    def __init__(self):
        self._title = "Handle"

    def draw(self):
        print("Start drawing with Handle")


stationary = Stationery()
stationary.draw()
pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()
