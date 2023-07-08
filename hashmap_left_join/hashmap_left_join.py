def left_join(hashmap1, hashmap2):
    """
    Perform a LEFT JOIN operation on two hashmaps.

    Args:
        hashmap1 (dict): The first hashmap with word strings as keys and corresponding values.
        hashmap2 (dict): The second hashmap with word strings as keys and corresponding values.

    Returns:
        list: A list of lists representing the joined data. Each inner list contains the key from hashmap1,
              the value from hashmap1, and the value from hashmap2. If a key doesn't exist in hashmap2,
              the third element in the inner list is None.
    """
    result = []
    for key in hashmap1:
        row = [key, hashmap1[key], hashmap2.get(key)]
        result.append(row)
    return result
