# Linear search


def linear_search(array, num):
    for i in range(len(array)):
        if array[i] == num:
            return i

    return -1


def main():
    a = [45, 67, -2, 33, -44, 134, -67]
    print(a)
    for n in [1, 0, -1, 2, -2, 134, 67, -67]:
        print("%5d index? %d" % (n, linear_search(a, n)))


main()
