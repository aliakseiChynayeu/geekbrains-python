# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод. Задачу
# можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
# завершать скрипт.
import time


class TrafficLight:
    __color: str
    colors = ["red", "yellow", "green"]

    def running(self, color: str):
        if color in TrafficLight.colors:
            self.__color = color
            print(f"Traffic light is {color}")
        else:
            print(f"Wrong color, next is allowed : {TrafficLight.colors}")


trafficLight = TrafficLight()
for x in range(5):
    trafficLight.running(TrafficLight.colors[0])
    time.sleep(7)
    trafficLight.running(TrafficLight.colors[1])
    time.sleep(2)
    trafficLight.running(TrafficLight.colors[2])
    time.sleep(5)
trafficLight.running("blue")
