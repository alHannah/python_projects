row = int(input("Enter Row Size: "))
col = int(input("Enter Column Size: "))

multi_array = []

count = 1

for i in range(row):
    row_list = []
    for j in range(col):
        row_list.append(count)
        count += 1
        print(row_list[j], end=" ")
    multi_array.append(row_list)
    print()
    print()

# You can uncomment the following lines to display the 2D array
for row_list in multi_array:
    print(" ".join(map(str, row_list)))
