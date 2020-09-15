# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].
import random

initial_list = []
for i in range(0, 20):
    initial_list.append(random.randrange(0, 1000))
print(initial_list)

result_list = [value for index, value in enumerate(initial_list) if value > initial_list[index-1]]

print(result_list)
