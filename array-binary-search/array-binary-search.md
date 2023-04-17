# array-binary-search

## Summary
The binary search algorithm is a popular algorithm used to search for a particular item in a sorted list. It works by repeatedly dividing in half the portion of the list that could contain the target item, until you've narrowed down the possible locations to just one.

## Description
The binary search algorithm takes advantage of the fact that the input list is already sorted. It starts by examining the middle item of the list. If the target value is less than the middle item, then the algorithm will repeat the search on the left half of the list. If the target value is greater than the middle item, then the algorithm will repeat the search on the right half of the list. By dividing the search space in half at each step, the binary search algorithm can quickly locate the target item in the list.

## Approach & Efficiency
The binary search algorithm takes advantage of the fact that the input list is sorted, which allows it to quickly narrow down the possible locations of the target item. The algorithm has a time complexity of O(log n) because it divides the search space in half at each step, which reduces the search time significantly.



## Approach:
We will start by finding the middle element of the array. If this element matches the search key, we will return its index. If the middle element is greater than the search key, we will perform a binary search on the left half of the array. If the middle element is less than the search key, we will perform a binary search on the right half of the array. We will continue this process until we either find the search key or determine that it is not in the array.

## Problem Domain:
We are given a sorted array of integers and a search key. Our task is to implement a binary search algorithm to search for the search key in the array. If the search key is found, we return the index of the element. If the element is not in the array, we return -1.
## Visual
![binary-and-linear-search-animations](https://user-images.githubusercontent.com/60603704/230966462-7d17e971-723f-4a04-8406-1930bb8ba8db.gif)
## Algorithm:
The steps of the algorithm are as follows:
Set the left pointer to the first index of the array
Set the right pointer to the last index of the array
While the left pointer is less than or equal to the right pointer:
Set the mid pointer to the index halfway between the left and right pointers
If the element at the mid pointer is equal to the search key, return the mid pointer
If the element at the mid pointer is greater than the search key, set the right pointer to the index to the left of the mid pointer
If the element at the mid pointer is less than the search key, set the left pointer to the index to the right of the mid pointer
If we haven't returned by this point, the search key is not in the array. Return -1.
## Big O:
The time complexity of binary search is O(log n) since we divide the search space in half at each step. The space complexity is O(1) since we are not using any additional space besides the input array.

## Pseudocode
```
function binarySearch(arr, key):
  left = 0
  right = length(arr) - 1
  while left <= right:
    mid = floor((left + right) / 2)
    if arr[mid] == key:
      return mid
    else if arr[mid] > key:
      right = mid - 1
    else:
      left = mid + 1
  return -1

```
## Code
```
def binary_search(arr, key):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    return -1

```

## Test:
We can test our function with the following test cases:
```
# Happy Path
assert binary_search([4, 8, 15, 16, 23, 42], 15) == 2
assert binary_search([-131, -82, 0, 27, 42, 68, 179], 42) == 4

# Expected Failure
assert binary_search([11, 22, 33, 44, 55, 66, 77], 90) == -1
assert binary_search([1, 2, 3, 5, 6, 7], 4) == -1

```
# Feature Tasks
1. Implement a binary search function that takes in a sorted array and a search key, and returns the index of the array's element that is equal to the value of the search key, or -1 if the element is not in the array.

2. The function should use a binary search algorithm and not utilize any built-in methods available to your programming language.

## Unit Tests
### Happy Path

Test for a successful search:
```
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
key = 10
assert BinarySearch(arr, key) == 4

```
### Expected Failure
Test for a search key not in the array:

```
arr = [1, 3, 5, 7, 9]
key = 6
assert BinarySearch(arr, key) == -1

```

### Edge Case
Test for an empty array:

```
arr = []
key = 5
assert BinarySearch(arr, key) == -1

```

Test for an array with a single element:

```
arr = [5]
key = 5
assert BinarySearch(arr, key) == 0

```

Test for an array with all elements identical:

```
arr = [10, 10, 10, 10, 10, 10]
key = 10
assert BinarySearch(arr, key) == 2

```
These tests should cover the expected behavior of the binary search function for various inputs.
