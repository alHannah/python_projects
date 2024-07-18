# #!/bin/python3
#
# import math
# import os
# import random
# import re
# import sys


#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Find the maximum element in the array
    max_element = max(arr)

    # Create a counting array to store the count of each element
    count = [0] * (max_element + 1)

    # Count the occurrences of each element in the input array
    for num in arr:
        count[num] += 1

    # Reconstruct the sorted array
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])

    return sorted_arr


# Input size
n = int(input("N: ").strip())

# Input array
arr = list(map(int, input("ARR: ").rstrip().split()))

# Perform counting sort
result = countingSort(arr)

# Print the sorted array
print(' '.join(map(str, result)))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input().strip())
#
#     arr = list(map(int, input().rstrip().split()))
#
#     result = countingSort(arr)
#
#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')
#
#     fptr.close()
