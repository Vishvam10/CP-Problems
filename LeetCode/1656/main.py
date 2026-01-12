"""
DIFFICULTY : medium
TAGS : array, hash table, design, data stream
"""


class OrderedStream:
    def __init__(self, n):
        self.arr = [None] * n
        self.ptr = 0

    def insert(self, idKey, value):
        idKey -= 1
        self.arr[idKey] = value
        if self.ptr < idKey:
            return []
        else:
            while self.ptr < len(self.arr) and self.arr[self.ptr] is not None:
                self.ptr += 1
            return self.arr[idKey : self.ptr]
