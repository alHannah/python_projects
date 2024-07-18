name_list = []
in_entry = True
while in_entry:
    name = input("Name: ")
    new = input("Another entry?[y][n]: ").lower()
    name_list.append(name)

    if new == "n":
        in_entry = False

for every_name in name_list:
    print(every_name)

