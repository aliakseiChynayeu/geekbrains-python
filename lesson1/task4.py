# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
number = int(input("Введите целое положительное число >>> "))
max_number = 0
current_number = number
while True:
    if max_number < current_number % 10:
        max_number = current_number % 10
    if current_number // 10 == 0:
        break
    current_number //= 10
print("Максимальная цифра числа {}, равна {}".format(number, max_number))
