
# Not printing all elements base on the index
names = ["Lance", "Dominic", "Bret", "Algen", "Lineth", 90]
print(names[2:])
# Printing all including the above list
nums = [19, 20, 18, 18, 19]
all = [names, nums]
print(all)

nums.append(20) # Adding element to the last
print(nums)

nums.insert(0, 999) # Inserting element in a certain index
print(nums)

nums.remove(999) # Removing element
print(nums)

del nums[4:] # Deleting rows
print(nums)

nums.extend([111, 222, 000]) # Adding multiple Elements in the last part
print(nums)

# Printing the maximum and minimum element
print(min(nums))
print(max(nums))

print(sum(nums)) # Printing the sum of all Elements

# Sorting or Printing elements in ascending order
nums.sort()
print(nums)

# Putting User Input into the list
n1 = input("Enter your name: ")
n2 = input("Enter your name: ")
n3 = input("Enter your name: ")
n = [n1, n2, n3]
n4 = input("Enter your name: ")
n.append(n4)
n.insert(0, "Lineth")
print(n)
print(n[2])
