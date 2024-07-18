row = int(input("Row: "))
col = int(input("Column: "))

print(row)
print(col)
count = 1
arr = []

for i in range(1, row):
    for j in range(1, col):
        new = count++
        arr[i][j].appennd(new)
        print(arr)
