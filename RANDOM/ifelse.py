#bmi calculator applying if else statement

name = "al"
hight_m = 2
weight_kg = 90

bmi = weight_kg / (hight_m ** 2)
print("your bmi: ", bmi)

#condition
if bmi > 25:
    print(name)
    print("Check your Health.")
elif bmi < 22:
    print(name)
    print("Check your Health.")
else:
    print(name)
    print("Healthy.")