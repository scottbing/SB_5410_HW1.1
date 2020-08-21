# Python3 code to linearly search x in arr[].
# If x is present then return its location,
# otherwise return -1

import numpy as np


def search(arr, n, x):
    operations = 0
    for i in range(0, n):
        operations += 1
        if arr[i] == x:
            # print("linear ops:", operations)
            return i
    # print("linear ", operations)
    return -1;


# Python3 Program for recursive binary search.

# Returns index of x in arr if present, else -1
def binarySearch(arr, l, r, x):
    operations = 0
    while l <= r:
        operations += 1
        mid = l + (r - l) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            # print("binary ops:", operations)
            return mid

        # If x is greater , ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller , ignore right half
        else:
            r = mid - 1

    # if we reach here, then the element
    # was not present
    # print("binary ops:", operations)
    return -1


# Driver Code
if __name__ == "__main__":
    # Driver Code

    # generate an array of 'n' random numbers
    n = 200
    arr = np.random.choice(n, n, replace=False)
    # print(arr)

    # search item
    x = 10;
    n = len(arr)

    import timeit

    iter = 10

    ltime = timeit.timeit(lambda: search(arr, n, x), \
                          setup="from __main__ import search", number=iter)
    arr.sort()
    btime = timeit.timeit(lambda: binarySearch(arr, 0, n - 1, x), \
                          setup="from __main__ import binarySearch", number=iter)

    print("Linear search took:", ltime)
    print("Binary search took:", btime)
