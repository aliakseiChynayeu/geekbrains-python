# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.

class Car:
    _speed: int
    _color: str
    _name: str
    _is_police: bool

    def __init__(self, color: str, name: str):
        self._speed = 0
        self._color = color
        self._name = name
        self._is_police = False

    def go(self, speed: int):
        self._speed = speed
        print(f"Car {self._name} go with speed {self._speed}")

    def stop(self):
        self._speed = 0
        print(f"Car {self._name} is stopped")

    def turn(self, direction: str):
        print(f"Car {self._name} turned to {direction}")

    def show_speed(self):
        print(f"Car {self._name} has speed {self._speed}")


class TownCar(Car):
    def __init__(self, color: str, name: str):
        super().__init__(color, name)

    def go(self, speed: int):
        super().go(speed)
        if speed > 60:
            print("You've exceed speed limit for Town car")


class SportCar(Car):
    def __init__(self, color: str, name: str):
        super().__init__(color, name)


class WorkCar(Car):

    def __init__(self, color: str, name: str):
        super().__init__(color, name)

    def go(self, speed: int):
        super().go(speed)
        if speed > 40:
            print("You've exceed speed limit for Work car")


class PoliceCar(Car):

    def __init__(self, color: str, name: str):
        super().__init__(color, name)
        self._is_police = True


workCar = WorkCar("white", "skoda")
sportCar = SportCar("red", "lamborghini")
townCar = TownCar("green", "bmw")
policeCar = PoliceCar("black", "ford")

workCar.go(100)
sportCar.go(300)
townCar.go(30)
policeCar.go(310)

sportCar.stop()
workCar.go(40)
townCar.turn("left")