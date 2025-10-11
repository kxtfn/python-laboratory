a = 5
b = 80
squares = [x**2 for x in range(a, b+1)]
average = sum(squares) / len(squares)
print(f"Середнє арифметичне квадратів чисел від {a} до {b} = {average}")
