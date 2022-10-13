# Binary Search
# Upper & Lower Bound
# Midpoint

def bin_search(sequence, values):
    lower_bound = 0
    upper_bound = len(sequence) - 1

    while lower_bound <= upper_bound:
        midpoint = lower_bound + (upper_bound - lower_bound)
        midpoint_value = sequence[midpoint]

        if midpoint_value == values:
            return midpoint
        elif values < midpoint_value:
            upper_bound = midpoint - 1
        else:
            lower_bound = midpoint + 1
    return None

list = [10, 30, 561, 634, 82, 1, 3 ,77]
to_find = 10

value = bin_search(list, to_find)

print("Element found at index: ", value)