from array import *

# Big 'I' - unsigned
# Small 'i' - signed
# 'u' - unicode


# Number Array using For Loop
nums = array('i', [10, 20, -30, 40 ,50]) # Big 'I'(unsigned) do not accept negative number
nums.append(60)
nums.remove(50)
nums.insert(0, 100)
nums.reverse()
for i in nums:
    print(i)

# Copying the Array above
arr = array(nums.typecode, (a * a for a in nums)) # a * a means the square of each element
z = 0
while z < len(arr):
    print(arr[z])
    z += 1


# Character Array using For Loop
char = array('u', ['L', 'A', 'N', 'C', 'E'])
for a in char:
    print(a)


# Number Array using While Loop
nums = array('i', [10, 20, -30, 40, 50])
a = 0
while a < len(nums):
    print(nums[a])
    a += 1

# Character Array using While Loop
char = array('u', ['L', 'A', 'N', 'C', 'E'])
b = 0
while b < len(char):
    print(char[b])
    b += 1


# Sorting an Array
nums = array('i', [10, 60, -30, 40 ,50])
a = nums.tolist()
a.sort()
for i in a:
    print(i)


# Array and User input puting inputs in the array
num1 = int(input('Enter a number: '))
num2 = int(input('Enter a number: '))
num3 = int(input('Enter a number: '))
r = array('i', [num1, num2, num3])
for i in r:
    print(i)

# Array and User input that allows user to decide the length of the array
r = array('i', [])
n = int(input('Enter the length of the Array: '))
for i in range(n):
    x = int(input('Enter the elements of the Array: '))
    r.append(x)
for a in r:
    print(a)

# Search element in array by showing its index
num1 = int(input('Enter a number: '))
num2 = int(input('Enter a number: '))
num3 = int(input('Enter a number: '))
r = array('i', [num1, num2, num3])
put = int(input('Enter a number you want to search: '))
k = 0
for e in r: # Manual Search
    if e == put:
        print("The index is: ", k)
        break;
    k += 1

print("The index is: ", r.index(put)) # Using function


# Assignment 1 - Deleting certain index
y = array('i', [10, 20, 30, 40, 50])

for i in y:
    if i == y[2]:
        continue
    print(i)

# Assignment 2 - Printing values in array in reverse order
y = array('i', [15, 25, 35, 45, 55])
for i in range(4, -1, -1):
    print(y[i])


# Assignment 3 - Adding two arrays using For Loop
ar1 = array('i', [5,6,7,8,9])
ar2 = array('i', [11,12,13,14,15])
for a in range(0, 5):
        print(ar1[a] + ar2[a])

# Assignment 4 - Finding the maximum element in the array
r = array('i', [])
n = int(input('Enter the length of the Array: '))
for i in range(n):
    x = int(input('Enter the elements of the Array: '))
    r.append(x)
print(max(r))


# Concat two arrays (Error ky walay import numpy)
ar1 = array('i', [5,6,7,8,9])
ar2 = array('i', [11,12,13,14,15])
for a in range(0, 5):
        print(concatenate([ar1, ar2]))
        


# Multideminsional Array
my = array([
            [1, 2, 3],
            [4, 5, 6]
            ])
print(my)
print(my.shape) # Printing the shape/columns and rows
print(my.size()) # Printing Size of the elements

my2 = my.flatten() # Converting to 1 Dimentional
my3 = my2.reshape(3, 2) # Customizing columns and rows
my3 = my2.reshape(2, 3, 2) # Customizing columns and rows and adding dimention

# Matrix (same as Array)
m = matrix('1 2 3') # 1 rows and 3 columns
print(m)
m = matrix('1 2 3 ; 4 5 6') # 3 x 3
print(m)
m = matrix('1 2 ; 3 4 ; 5 6') # 3 x 2
print(m)


