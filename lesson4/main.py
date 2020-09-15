import sys
from lesson4 import task1

try:
    file, hours, rate, bonus = sys.argv
except ValueError:
    print("Invalid args. Expected : hours, rate and bonus")
    exit()

print(task1.calc_salary(hours, rate, bonus))