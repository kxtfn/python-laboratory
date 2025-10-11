import math

def calc_expression(x, y):
    return math.cos(x) ** 2 + math.sin(y) ** 2

def sum_of_squares(N):
    return sum(i**2 for i in range(1, N+1))

x = float(input("Введіть x: "))
y = float(input("Введіть y: "))
z = calc_expression(x, y)
print(f"z = {z}")

N = int(input("Введіть N: "))
S = sum_of_squares(N)
print(f"S = {S}")
