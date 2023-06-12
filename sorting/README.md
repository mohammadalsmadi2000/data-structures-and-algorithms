## Explanation of Insertion Sort:
Insertion Sort is a simple sorting algorithm that builds the final sorted array one element at a time. It works by repeatedly inserting the current element into its correct position within the already sorted part of the array.



## Visual Step-through:

 `[8,4,23,42,16,15]` 

| Iteration | Array                 |
|-----------|-----------------------|
| 1         | [8]                   |
| 2         | [4, 8]                |
| 3         | [4, 8, 23]            |
| 4         | [4, 8, 23, 42]        |
| 5         | [4, 8, 16, 23, 42]    |
| 6         | [4, 8, 15, 16, 23, 42]|


**Efficiency**

- Time Complexity: `O(n^2)`

- Space Complexity: `O(1)`
  - No additional space is being created.




