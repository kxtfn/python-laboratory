def parne(a, x):
    i = 1
    while i < len(a):
        a.insert(i, x)
        i += 2
    print("Список після вставки:", a)

n = int(input("Введіть кількість елементів у списку: "))
a = []
for idx in range(n):
    val = input(f"Введіть елемент №{idx + 1}: ")
    a.append(val)
x = input("Введіть елемент, який потрібно вставляти на парні позиції: ")
parne(a, x)
