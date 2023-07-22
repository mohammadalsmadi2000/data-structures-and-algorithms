class Hashtable:
    """
    A simple hashtable implementation.
    """

    def __init__(self, size=10):
        """
        Initialize a hashtable with a given size.

        Args:
            size (int): The size of the hashtable (default: 10).
        """
        self.size = size
        self.table = [{} for _ in range(size)]

    def hash(self, key):
        """
        Compute the hash value for a given key.

        Args:
            key: The key to be hashed.

        Returns:
            int: The hash value.
        """
        return hash(key) % self.size

    def set(self, key, value):
        """
        Set a key-value pair in the hashtable.

        Args:
            key: The key to be set.
            value: The value to be associated with the key.
        """
        index = self.hash(key)
        bucket = self.table[index]
        bucket[key] = value

    def get(self, key):
        """
        Retrieve the value associated with a given key from the hashtable.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the key, or None if the key does not exist.
        """
        index = self.hash(key)
        bucket = self.table[index]
        return bucket.get(key)

    def has(self, key):
        """
        Check if a given key exists in the hashtable.

        Args:
            key: The key to check for existence.

        Returns:
            bool: True if the key exists, False otherwise.
        """
        index = self.hash(key)
        bucket = self.table[index]
        return key in bucket

    def keys(self):
        """
        Get a list of all keys in the hashtable.

        Returns:
            list: A list of all keys in the hashtable.
        """
        return [key for bucket in self.table for key in bucket.keys()]


if __name__=="__main__":
    pass