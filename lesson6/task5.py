# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

from lesson6.task4 import *

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