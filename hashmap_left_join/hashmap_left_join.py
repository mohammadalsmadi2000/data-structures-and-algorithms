class Hashmap:
    def __init__(self):
        self.hashmap = {}

    def put(self, key, value):
        self.hashmap[key] = value

    def get(self, key):
        return self.hashmap.get(key)

def left_join(hashmap1, hashmap2):
    result = []
    for key in hashmap1.hashmap:
        row = [key, hashmap1.get(key), hashmap2.get(key)]
        result.append(row)
    return result