import random


def print_valid_configuration(new):
    n = new

    # Generate a valid configuration for the spies
    configuration = []  # list of rows in numbers
    asterisk_row = []
    asterisk_col = []
    for rows in range(1, n + 1):  # print the number of rows
        configuration.append(rows)  # print the number from 1 to n plus 1
        asterisk_row.append("*")  # will print the asterisk

    int_configuration = len(configuration)
    for columns in range(int_configuration):
        asterisk_col.append("*")

    # Print the space-separated list of column numbers
    print(" ".join(map(str, asterisk_row)))

    for _ in range(int_configuration - 1):
        print(" ".join(map(str, asterisk_col)))

    random_s = []

    for _ in range(random.randint(2, 7)):
        rand_spy = random.choice(configuration)
        random_s.append(rand_spy)

    spy_grid = []
    for row in range(int_configuration):
        spy_row = []
        for col in range(int_configuration):
            if col + 1 in random_s and row + 1 in random_s:
                if col + 1 == random_s.index(row + 1) + 1:
                    spy_row.append("S")
                else:
                    spy_row.append("*")
            else:
                spy_row.append("*")
        spy_grid.append(" ".join(map(str, spy_row)))

    for row in spy_grid:
        print(row)


# Example usage:
print_valid_configuration(11)
