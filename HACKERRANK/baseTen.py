n = 5

def baseTwo(base):
    # ans =  base / 2
    return base / 2
    # ans = base %2
    # return base %2
    # print(ans)


newBase = baseTwo(n)

if newBase == 0:
    stillInBase = False
else:
    stillInBase = True


while(stillInBase):
    print("hi")
    baseTwo(newBase)