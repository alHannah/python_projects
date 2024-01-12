def max_element_after_operations(arr):
    if len(arr) == 1:
        return 1
        
        prev = arr[0]

    for i in range(1, len(arr)):
        # the diff is greater than 1
        # so we update the current value to be one greater than prev
        if arr[i] - prev > 1:
            arr[i] = prev + 1
        # update prev
        prev = arr[i]
    # max can be len(arr), otherwise return the max
    return len(arr) if max(arr) > len(arr) else max(arr)
    
# Example 1
arr1 = [2, 2, 1, 2, 1]
result1 = max_element_after_operations(arr1)
print(result1)  # Output: 2

# Example 2
arr2 = [100, 1, 1000]
result2 = max_element_after_operations(arr2)
print(result2)  # Output: 3

# Example 3
arr3 = [1, 2, 3, 4, 5]
result3 = max_element_after_operations(arr3)
print(result3)  # Output: 5
