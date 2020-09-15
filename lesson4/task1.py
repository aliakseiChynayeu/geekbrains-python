# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

def calc_salary(hours, rate, bonus):
    try:
        return float(hours) * float(rate) + float(bonus)
    except ValueError:
        print("Conversion error! Please check values that you've use.")
        return 0;
