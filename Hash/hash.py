class Hashtable:
    def __init__(self, size=10):
        self.size = size
        self.table = [{} for _ in range(size)]

    def hash(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        index = self.hash(key)
        bucket = self.table[index]
        bucket[key] = value

    def get(self, key):
        index = self.hash(key)
        bucket = self.table[index]
        return bucket.get(key)

    def has(self, key):
        index = self.hash(key)
        bucket = self.table[index]
        return key in bucket

    def keys(self):
        return [key for bucket in self.table for key in bucket.keys()]
