# year = int(input("Year: "))

# print(year)


def print_week():
    week = {
        "w1": "Sun",
        "w2": "Mon",
        "w3": "Tue",
        "w4": "Wed",
        "w5": "Thu",
        "w6": "Fri",
        "w7": "Sat",
    }

    for i in week:
        print(" ", week[i], end=' ')


def print_month():
    month = {
        "m1": "January",
        "m2": "february",
        "m3": "March",
        "m4": "April",
        "m5": "May",
        "m6": "June",
        "m7": "July",
        "m8": "August",
        "m9": "September",
        "m10": "October",
        "m11": "November",
        "m12": "December",
    }

    key = list(month.keys())
    m = 0

    while m < len(key):
        key_index = key[m]
        print("\t\t\t\t", month[key_index], end=' ')
        print("")
        print_week()
        print("")
        print("")
        m += 1

print_month()
# print_week()