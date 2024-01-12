def in_number(n):
    return n%2 == 0

num = [1, 2, 3, 4]
res = any(map(in_number, num))
print(res)