size = 7
arr = []
for i in range(size):
    row = []
    for j in range(size):
        value = 1 if i % 2 == 0 else 0
        row.append(value)
    arr.append(row)

for row in arr:
    print(' '.join(str(x) for x in row))
