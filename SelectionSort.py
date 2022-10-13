# Selection Sort
# Finding first the smallest value in the list
# Swapping by putting the smaller value to the first

def SelectionSort(nums):
    indexLength = range(0, len(nums) - 1)

    for i in indexLength:
        minValue = i

        for j in range(i + 1, len(nums)):
            if nums[j] < nums[minValue]:
                minValue = j

            if minValue != i:
                nums[minValue], nums[i] = nums[i], nums[minValue]

    return nums

print(SelectionSort([9, 1, 5, 2, 9, 1 ,6 ,3 ,1 , 5]))
