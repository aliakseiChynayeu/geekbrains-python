# Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

number = int(input("Введите число >>> "))
number2 = int(input("Введите ещё одно число >>> "))
string = input("Введите строку >>> ")
string2 = input("Введите ещё одну строку >>> ")
print("Вы ввели числа {} и {}, а так же строки {} и {}".format(number, number2, string, string2))
