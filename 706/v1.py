class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size
    
    def _find_index(self, key: int, bucket: list) -> int:
        for i, (k, v) in enumerate(bucket):
            if k == key:
                return i
        return -1

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]

        i = self._find_index(key, bucket)
        if i != -1:
            bucket[i][1] = value
        else:
            bucket.append([key, value])

    def get(self, key: int) -> int:
        index = self._hash(key)
        bucket = self.buckets[index]

        i = self._find_index(key, bucket)
        if i != -1:
            return bucket[i][1]
        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]

        i = self._find_index(key, bucket)
        if i != -1:
            bucket.pop(i)
