def this_int(n):
    return n%2 == 0

num = [1, 2, 3, 4, 5]
result = any(map(this_int, num))

print(result)