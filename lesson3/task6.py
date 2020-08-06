def my_func(input_str):
    """
    Функция для перевода слов в строке с прописной буквы
    :param input_str: строка со словами
    :return: строка со словами, начинающимися с прописной буквы
    """
    def int_func(word):
        """
        внутренняя функция, принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой
        :param word: слово для перевода
        :return: слово с прописной буквы
        """
        return word.capitalize()
    result = ""
    for w in input_str.split():
        result = result + int_func(w) + " ";
    return result


print(my_func("hello all!!!"))
print(my_func("test string for python lesson 3,  task 6 "))
