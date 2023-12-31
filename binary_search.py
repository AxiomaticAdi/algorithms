# Binary search

import math


def binary_search(array, num):
    # Handle empty arrays or arrays of one value
    if len(array) == 0:
        return -1
    if len(array) == 1:
        if array[0] == num:
            return 0
        else:
            return -1

    # Send to search algo
    return search(array, num, 0, len(array) - 1)


def search(array, num, min, max):
    # Recursive base case: check last two values
    if (min == max) or (min + 1 == max):
        if array[min] == num:
            return min
        elif array[max] == num:
            return max
        else:
            return -1

    # Find middle of array
    middleIndex = min + math.floor((max - min) / 2)

    # Check middle value
    middleValue = array[middleIndex]
    if middleValue == num:
        # To find first index of match, decrement index if prior element matches
        while array[middleIndex - 1] == num:
            middleIndex -= 1
        return middleIndex
    elif num > middleValue:
        return search(array, num, middleIndex + 1, max)
    elif num < middleValue:
        return search(array, num, min, middleIndex - 1)


def main():
    a = [i for i in range(-1, 10, 2)]
    print(a)
    for n in [1, 0, -1, 2, -2, 4, 5, 6, 7, -67, 134]:
        print("%5d index? %d" % (n, binary_search(a, n)))


main()

# Pseudo

# Binary takes in array and target number
# returns search on array, num, 0, and len(array-1)

# Search function
# Finds middle

# Find middle of array
# if (len(array) % 2 == 0):

# check value at middle
# if index = target
#     return Index
# if index > target
# slice array
# if index < target
# slice and recursively call
