def calculate_sum(numbers):
    """
    Функция подсчета суммы введённых символов
    :param numbers: список ццифр
    :return: сумму цифр
    """
    res = 0
    for i in numbers:
        try:
            res += int(i)
        except ValueError:
            continue
    return res


is_quite = False
result = 0
print("Вводите строку цифрб разделённых пробелами. Для выхода введите символ !")
while not is_quite:
    print(f"Текущая сумма = {result}")
    input_str = input()
    if "!" in input_str:
        is_quite = True
        input_str = input_str.partition("!")[0]
    result += calculate_sum(input_str.split())
print(f"Символ выхода был введён! Общая сумма = {result}")
