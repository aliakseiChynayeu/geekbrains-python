# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
input_sec = int(input("Введите секунды >>> "))

hours = input_sec // 3600
if input_sec - (hours * 3600) > 0:
    minutes = (input_sec - (hours * 3600)) // 60
sec = input_sec - hours * 3600 - minutes * 60

print("{} секунд в переводе на чч:мм:сс равно : {}:{}:{}".format(input_sec, hours, minutes, sec))
