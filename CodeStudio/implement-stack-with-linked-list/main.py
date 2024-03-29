class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class Stack:
    # Write your code here
    def __init__(self):
        # Write your code here
        self.st = Node(-1)
        self.prev = None
        self.cur = self.st
        self.eles = 1

    def getSize(self):
        return self.eles

    def isEmpty(self):
        return True if (self.eles == 1) else False

    def push(self, data):
        temp = Node(data)
        self.cur.next = temp
        self.cur = self.cur.next
        self.prev = temp

        self.eles += 1

    def pop(self):
        if (self.prev):
            self.prev.next = self.cur.next
            self.eles -= 1

    def getTop(self):
        return self.cur
