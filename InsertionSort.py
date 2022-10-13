# Insertion Sort
# Swapping two elements at a time


def InsertionSort(nums):
    indexLength = range(1, len(nums))

    for i in indexLength:
        value = nums[i]

        while nums[i - 1] > value and i > 0:
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
            i = i - 1

    return nums


print(InsertionSort([10, 1, 9 ,12, 6, 4, 2 ,7]))