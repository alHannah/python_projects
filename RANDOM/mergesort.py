def mergesort(m, n, nums1, nums2):
    m = len(nums1)
    n = len(nums2)

    filteredm = [x for x in nums1 if x != 0]
    filteredn = [x for x in nums2 if x != 0]

    combined = filteredm + filteredn
    sort = combined.sort()
    print(sort)

nums1 = [0, 5, 2]
nums2 = [1, 0, 2, 3]
m = len(nums1)
n = len(nums2)
mergesort(m, n, nums1, nums2)
