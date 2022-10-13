# Linear Search
# Searching the Elements one by one


pos = 0

def linear_search(list, n):
    i = 0

    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i + 1

    return False

list = [128, 76, 1 ,4, 56, 120, 6, 9]
n = 56

if linear_search(list, n):
    print("Found in index: ", pos)
else:
    print("Not Found")