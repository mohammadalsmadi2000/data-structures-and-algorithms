# Problem Domain: 
We want to write a function that reverses the order of elements in an array.

# Visual:

Input: [1, 2, 3, 4, 5]

Output: [5, 4, 3, 2, 1]
```
   [1, 2, 3, 4, 5]                 [5, 4, 3, 2, 1]       
        i   j                          i   j              
        ↓   ↓                          ↓   ↓              
   [1, 2, 3, 4, 5]      →      [5, 2, 3, 4, 1]             
    i       j                      i       j          
    ↓       ↓                      ↓       ↓          
   [5, 2, 3, 4, 1]      →      [5, 4, 3, 2, 1]             
       i   j                         i   j      
       ↓   ↓                         ↓   ↓      
   [5, 4, 3, 2, 1]      →      [5, 4, 3, 2, 1]             
```

# Algorithm: 
One way to reverse an array is to use two pointers, one pointing to the beginning of the array and the other pointing to the end of the array. Swap the values of the elements pointed by the two pointers, increment the first pointer and decrement the second pointer until the first pointer is greater than or equal to the second pointer.

# Big O:
 The time complexity of this algorithm is O(N), where N is the number of elements in the array. The space complexity is O(1), because we are only modifying the input array in place.

 # Pseudocode:
 ```function reverseArray(arr):
    i = 0
    j = length(arr) - 1
    while i < j:
        swap arr[i] with arr[j]
        i = i + 1
        j = j - 1
    return arr
  ```  

# Code:

```
def reverseArray(arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr
```
# Test:

```
print(reverseArray([1, 2, 3, 4, 5]))   # Output: [5, 4, 3, 2, 1]
print(reverseArray([]))                # Output: []
print(reverseArray([1]))               # Output: [1]
```