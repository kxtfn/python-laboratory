a = int(input("Введіть значення A: "))
while not (1 <= a <= 100):
    a = int(input("Введіть значення A знову (1-100): "))

b = int(input("Введіть b: "))
while not (1 <= b <= 100):
    b = int(input("Введіть значення B знову (1-100): "))

if a > b:
    x = b / a + 61
elif a == b:
    x = -5
else:
    x = (b - a) / b

print(f"Значення X = {x}")
