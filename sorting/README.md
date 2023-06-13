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

![Screen Recording - June 12, 2023](https://github.com/mohammadalsmadi2000/data-structures-and-algorithms/assets/60603704/8b856b62-b549-4c7c-9103-1fa722440054)

**Efficiency**

- Time Complexity: `O(n^2)`

- Space Complexity: `O(n) in the worst case`
 



