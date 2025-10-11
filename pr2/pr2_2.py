import math
from pr2_1 import sum_of_squares

def calc_expression(x, y):
    return math.cos(x) ** 2 + math.sin(y) ** 2

x = float(input("Введіть x: "))
y = float(input("Введіть y: "))
z = calc_expression(x, y)
print(f"z = {z}")

N = int(input("Введіть N: "))
S = sum_of_squares(N)
print(f"S = {S}")
