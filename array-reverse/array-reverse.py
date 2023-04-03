def reverseArray(arr):
    """
    Reverses the order of elements in an array.
    """
    i, j = 0 ,len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr

#print(reverseArray([1, 2, 3, 4, 5, 6]))