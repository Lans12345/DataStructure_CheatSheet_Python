# Queue
# First in, First out

from collections import deque 

q = deque() # Assigning "deque" method to "q" variable

q.appendleft(10) # AppendLeft method
q.appendleft(5)
q.appendleft(15)

q.pop() # Removing the first element in the list
print(q)
q.extendleft([100]) # Extend Left - putting element in the first part

for i in q: # Printing the elements
    print(i)




