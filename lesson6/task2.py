# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод
# расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса
# асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу
# метода. Например: 20м*5000м*25кг*5см = 12500 т


class Road:
    __length: float
    __width: float
    __weight = 25
    __height = 5

    def __init__(self, length: float, width: float):
        self.__length = length
        self.__width = width

    def totalWeight(self) -> float:
        return self.__width*self.__length*Road.__height*Road.__weight/1000

road = Road(5000, 20)

print(f"total weight of road is {road.totalWeight()} t")
