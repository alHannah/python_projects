num_of_rows = 5
k = 0
for i in range(1, num_of_rows + 1):
    for space in range(1, (num_of_rows - 1) + 1):
        print(end = " ")
    while k != (2 * i - 1):
        print("* ", end = "")
        k += 1
    k = 0
    print()