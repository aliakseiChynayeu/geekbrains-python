def user_data(name, last_name, year, city, phone, email):
    """
    Функция для вывода данных
    :param name: Имя
    :param last_name: Фамилия
    :param year: год рождения
    :param city: город
    :param phone: телефон
    :param email: имейл
    Выводит на экран сообщение с введёнными данными
    """
    print(f"Имя: {name}, Фамилия: {last_name}, Год рождения : {year}\nГород : {city}, Имейл: {email}, Телефон: {phone}")


user_data(name="Петр", last_name="Петров", year=1986, city="Москва", phone="546565655", email="a@a.a")
