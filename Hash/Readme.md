## Problem Domain
We want to implement a Hashtable class with the following methods:
- `set(key, value)`: hashes the key and sets the key-value pair in the table, handling collisions as needed.
- `get(key)`: retrieves the value associated with a given key in the table.
- `has(key)`: checks if a key exists in the table.
- `keys()`: returns a collection of all unique keys in the table.
- `hash(key)`: returns the index in the collection for a given key.

## Big O Analysis
- `set(key, value)`: the worst case, it can be O(n) if there are many collisions in the same bucket.
- `get(key)`: the worst case, it can be O(n) if there are many collisions in the same bucket.
- `has(key)`: the worst case, it can be O(n) if there are many collisions in the same bucket.
- `keys()`: The time complexity is O(n), where n is the number of key-value pairs in the Hashtable.
- `hash(key)`: The time complexity is O(1), as it involves a simple hash function.


