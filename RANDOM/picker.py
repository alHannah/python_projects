import random

name_list = ["prims", "al", "RA", "tine", "anne"]

for _ in name_list:
    print(f"Next supply will be bought by: {_} Order number [{random.randint(1, 5)}]")
