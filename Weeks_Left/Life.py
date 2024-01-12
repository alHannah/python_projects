import os

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

time_dictionary = {
    "months": 12,
    "weeks": 52,
    "days": 365
}

life_dictionary = {}
operating = True

def life_calculator(age, life_expectancy):
    for time in time_dictionary:
        life_left = life_expectancy - age
        new = time_dictionary[time] * life_left
        life_dictionary = time_dictionary[time] = new

    print(time_dictionary)


while operating:
    age = int(input("How Old are you?\n:"))
    life_expectancy = int(input("In what age you think you will last?\n:"))

    time_left = life_calculator(age, life_expectancy)
    print(time_left)

    operate = input("Do you want to operate this program again?\n[yes]  [no]\n:").lower()
    if operate == 'no':
        operating = False

clear()