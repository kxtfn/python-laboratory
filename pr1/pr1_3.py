N = int(input("Введіть N ( 1 < N <9): "))
print("Виберіть тип виводу:")
print("1 — числа")
print("2 — зірочки *")
print("3 — решітки #")
choice = input("Ваш вибір: ")

for i in range(1, N + 1):
    for j in range(1, i + 1 ):
        if choice == "1":
            print(j, end=" ")
        elif choice == "2":
            print("*", end=" ")
        elif choice == "3":
            print("#", end=" ")
        else:
            print("?", end=" ")
    print()
