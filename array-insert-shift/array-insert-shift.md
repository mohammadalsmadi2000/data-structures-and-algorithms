# Problem Domain: 
The problem is to write a function called insertShiftArray that takes in an array and a value to be added. The function should add the new value at the middle index of the array, without using any of the built-in methods available in the programming language. The function should then return the updated array.

# Visual:
```
Input:
[2, 4, 6, -8], 5

Output:
[2, 4, 5, 6, -8]

Input:
[42, 8, 15, 23, 42], 16

Output:
[42, 8, 15, 16, 23, 42]
```

# Algorithm: 
Here is a possible algorithm to solve the problem:

Calculate the length of the input array.
Calculate the middle index of the input array by dividing the length of the array by 2 and rounding up.
Create a new empty array to store the result.
Loop through the original array up to the middle index and append each element to the result array.
Append the new value to the result array.
Loop through the original array from the middle index to the end and append each element to the result array.
Return the result array.

# Big O:
 Time Complexity: The time complexity of this algorithm is O(n), where n is the length of the input array. This is because we loop through the array twice, once up to the middle index and once from the middle index to the end. However, since we only loop through half of the array in each iteration, the time complexity is effectively O(n/2), which simplifies to O(n).
Space Complexity: The space complexity of this algorithm is also O(n), since we create a new array to store the result.

 # Pseudocode:
 ```
 function insertShiftArray(arr, value):
  length = arr.length
  middleIndex = round(length / 2)
  result = []
  for i from 0 to middleIndex - 1:
    result.push(arr[i])
  result.push(value)
  for i from middleIndex to length - 1:
    result.push(arr[i])
  return result
  ```  

# Code:

```
def insertShiftArray(arr, val):
  
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
```
# Test:

```
def test_insertShiftArray():
    assert insertShiftArray([2, 4, 6, -8], 5) == [2, 4, 5, 6, -8]
    assert insertShiftArray([42, 8, 15, 23, 42], 16) == [42, 8, 15, 16, 23, 42]
    assert insertShiftArray([], 1) == [1]
    assert insertShiftArray([1], 2) == [1, 2]
    assert insertShiftArray([1, 2], 3) == [1, 3, 2]
    assert insertShiftArray([1, 2, 3], 4) == [1, 2, 4, 3]
    assert insertShiftArray([1, 2, 3, 4], 5) == [1, 2, 5, 3, 4]
```