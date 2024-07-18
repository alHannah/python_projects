print("RUNNING SUM OF 1 D ARRAY")

list_of_nums = [1,4,6,13,14,15]

# printing the sum of each element in the list

comulative_sum = 0

for num in list_of_nums:
    comulative_sum = num + comulative_sum
    print(comulative_sum, end = " ")