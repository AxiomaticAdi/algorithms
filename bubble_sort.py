def makeSwap(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp


def bubble_sort(array):
    # Count how many times we've run bubble sort
    loopCounter = 0

    while loopCounter < len(array):
        leftIndex = 0
        rightIndex = 1

        # Each individual bubble sort run
        while rightIndex < len(array):
            if array[leftIndex] > array[rightIndex]:
                makeSwap(array, leftIndex, rightIndex)
            leftIndex += 1
            rightIndex += 1
        loopCounter += 1

    return array


def main():
    arrays = [
        [45, 67, -2, 33, 0, -44, 134, -67],
        [i for i in range(10)],
        [i for i in range(10, -1, -1)],
    ]

    for a in arrays:
        print("Unordered:", a)
        print("Sorted:   ", bubble_sort(a))


main()
