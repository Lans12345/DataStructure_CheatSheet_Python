# Quick Sort
# Pivoting

def quickSort(nums):
    length = len(nums)
    if length <= 1:
        return nums
    else:
        pivot = nums.pop()

    numsLow = []
    numsHigh = []

    for item in nums:
        if item > pivot:
            numsHigh.append(item)
        else:
            numsLow.append(item)

    return quickSort(numsLow) + [pivot] + quickSort(numsHigh)


print(quickSort([3, 5, 1, 2, 7, 5, 1, 9, 4, 3]))