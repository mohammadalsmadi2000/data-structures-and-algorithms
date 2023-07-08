# hashmap-left-join

## Problem Domain

Given two hashmaps, perform a LEFT JOIN operation to combine the key-value pairs from both hashmaps. The first hashmap contains word strings as keys and synonyms as values, while the second hashmap contains word strings as keys and antonyms as values. The goal is to return a new data structure that holds the joined results based on the LEFT JOIN logic.


## Big O Analysis

The `hashmap-left-join` function has a time complexity of O(n), where n is the number of keys in the first hashmap. Since we iterate through each key in the first hashmap, the time complexity is directly proportional to the number of keys.

## Algorithm

1. Create an empty list called `result` to store the joined data.
2. Iterate through each key in the first hashmap.
3. For each key, retrieve the value from the first hashmap and the corresponding value from the second hashmap using the `get()` method.
4. Create a new row list containing the key, the value from the first hashmap, and the value from the second hashmap.
5. Append the row to the `result` list.
6. After iterating through all keys in the first hashmap, return the `result` list.

## Code

```python
def left_join(hashmap1, hashmap2):
    result = []
    for key in hashmap1:
        row = [key, hashmap1[key], hashmap2.get(key)]
        result.append(row)
    return result
```
