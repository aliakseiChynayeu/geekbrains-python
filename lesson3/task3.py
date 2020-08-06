def my_func(a, b, c):
    """
    Функция возвращает сумму 2-х максимальных чисел
    :param a: первое число
    :param b: второе число
    :param c: третье число
    :return: сумма 2-ч максимальных чисел
    """
    if a > b or a > c:
        if b > c:
            return a + b
        else:
            return a + c
    else:
        return b + c


# Тестовые данные для функции
print(my_func(3, 7, 0))
print(my_func(7, 1, 12))
print(my_func(1, 1, 1))
print(my_func(1, 12, 13))
