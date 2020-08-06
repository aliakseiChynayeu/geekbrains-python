def divide(a, b):
    """
    Функция деления 2 чисел
    :param a: Делимое
    :param b: Делитель
    :return: Результат деления a/b
    Вывод на экран ошибки при делении на 0
    """
    try:
        return a / b
    except ZeroDivisionError:
        print("Деление на 0!!!")


a = int(input("введите делимое >>> "))
b = int(input("введите делитель >>> "))
result = divide(a, b)
if result is not None:
    print(f" {a} / {b} = {result:.3f}")
