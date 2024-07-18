num = [1, 6, 2, 2, 4, 8]
target = 3

output = []

for i in range(len(num)-1):
    for j in range(i+1, len(num)):
        if len(output) > 2:
            output.append("and")
        if num[i] + num[j] == target:
            output.append(i)
            output.append(j)


print(output)
