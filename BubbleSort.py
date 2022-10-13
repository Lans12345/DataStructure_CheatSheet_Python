# Bubble Sort
# Swapping

def bubbleSort(nums):
    indexLength = len(nums) - 1
    sort = False

    while not sort:
        sort = True
        for i in range(0, indexLength):
            if nums[i] > nums[i + 1]:
                sort = False
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

    return nums


print(bubbleSort([7, 8, 9, 1, 6, 1, 3, 2 ,4]))