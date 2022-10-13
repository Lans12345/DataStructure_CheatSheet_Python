# Stack
#Last in, First out

from collections import deque


nums = []
nums.append(15) # Adding a value
nums.append(5) # Adding a value
nums.append(10) # Adding a value


print(nums)
print(nums.pop()) # Removing the last value in the stack
print(nums)

print(nums.__contains__(5)) # Contains method - return True or False

nums.insert(0, 100) # Insert Method
print(nums)

print(nums.index(15)) # Index Method

nums.extend([1000]) # Extend Method
print(nums)



# Implementing Stack through Class
class Stack:
    def __init__(self):
        self.container = deque
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container) == 0
    def size(self):
        return len(self.container)
    


