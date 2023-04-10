
import math
def insertShiftArray(arr, val):
    """
    Given an array and a value, adds the value at the middle index of the array
    and returns the resulting array. If the array has an odd number of elements,
    the value is added at the exact middle index. If the array has an even number
    of elements, the value is added at the index to the right of the middle.
    """
    n = len(arr)
    mid = math.ceil(len(arr)//2)
    last=arr[len(arr)-1]

    # Shift all elements to the right of the middle index one position to the right
    for i in range(n-1, mid, -1):
        arr[i] = arr[i-1]

    # Insert the new value at the middle index
    arr[mid] = val
    arr.append(last)
    return arr



def removeShiftArray(arr):
    """
    Given an array, removes the element at the middle index and returns the resulting array.
    If the array has an odd number of elements, the element at the exact middle index is removed.
    If the array has an even number of elements, the element at the index to the left of the middle
    is removed.
    """
    n = len(arr)
    mid = math.floor(len(arr)//2)

    # Shift all elements to the right of the middle index one position to the left
    for i in range(mid, n-1):
        arr[i] = arr[i+1]

    # Set the last element to None to remove it from the array
    arr[n-1] = None

    return arr


# print(insertShiftArray([1,2,8,3,4,5])) # result :[1,2,8,3,4]