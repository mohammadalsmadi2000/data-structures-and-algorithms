class Hashtable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        index = self.hash(key)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        index = self.hash(key)
        bucket = self.table[index]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def has(self, key):
        index = self.hash(key)
        bucket = self.table[index]
        for k, _ in bucket:
            if k == key:
                return True
        return False

    def keys(self):
        keys = []
        for bucket in self.table:
            for k, _ in bucket:
                keys.append(k)
        return list(set(keys))
