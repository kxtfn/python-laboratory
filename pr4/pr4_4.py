def swap(lst):
    for i in range(1, len(lst), 2):
        lst[i], lst[i-1] = lst[i-1], lst[i]
    print("Список після обміну:", lst)

n = int(input("Введіть кількість елементів у списку: "))
lst = []
for idx in range(n):
    val = input(f"Введіть елемент №{idx + 1}: ")
    lst.append(val)
swap(lst)
