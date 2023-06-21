## Problem Domain:
Implement the mergesort algorithm to sort an array of positive and negative integers.

## Visual:
![Merge_sort_algorithm_diagram](https://github.com/mohammadalsmadi2000/data-structures-and-algorithms/assets/60603704/d4379533-6617-4fbc-a2ad-d5a907e15720)


## Algorithm:
1. If the array has fewer than two elements, return the array as it is already sorted.
2. Divide the array into two halves.
3. Recursively call mergesort on each half to sort them.
4. Merge the two sorted halves back together:
   - Create an empty result array.
   - Compare the first elements of the two sorted halves.
   - Append the smaller element to the result array and remove it from its original array.
   - Repeat the previous step until one of the arrays is empty.
   - Append the remaining elements of the non-empty array to the result array.
5. Return the merged result array.

## Test:
Input: [38, 37, 43, 3, 9, 82, 10]
Expected Output: [3, 9, 10, 37, 38, 43, 82]

## Code:
```python
def merge_sort(arr):
  
    if len(arr) < 2:
        return arr


    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

   
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

   
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left_sorted) and right_index < len(right_sorted):
        if left_sorted[left_index] < right_sorted[right_index]:
            result.append(left_sorted[left_index])
            left_index += 1
        else:
            result.append(right_sorted[right_index])
            right_index += 1

   
    result.extend(left_sorted[left_index:])
    result.extend(right_sorted[right_index:])

    return result

# Test the mergesort function
input_array = [38, 37, 43, 3, 9, 82, 10]
sorted_array = merge_sort(input_array)
print(sorted_array)
```

# Big O:
Time Complexity: The mergesort algorithm has a time complexity of O(n log n) as it divides the array into halves and merges them back together recursively. Each merge operation takes linear time.
Space Complexity: The space complexity is O(n) as the algorithm uses additional space to store the divided subarrays during the recursion. However, the space usage is efficient, as at any given time, it only needs to store a maximum of n elements.
