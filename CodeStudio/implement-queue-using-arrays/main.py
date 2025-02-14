from typing import List


class Queue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.arr = [0] * 100001

    #  Enqueue (add) element 'e' at the end of the queue.
    def enqueue(self, e: int) -> None:
        if (self.rear + 1 < 100001):
            self.arr[self.rear] = e
            self.rear += 1

    #  Dequeue (retrieve) the element from the front of the queue.
    def dequeue(self) -> int:
        if (self.front == self.rear):
            return -1
        if (self.front < 100001):
            ele = self.arr[self.front]
            self.front += 1
            return ele
