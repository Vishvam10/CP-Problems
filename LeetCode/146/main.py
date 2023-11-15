class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.mp = {}

    def add_node(self, newnode):
        temp = self.head.next
        newnode.next = temp
        newnode.prev = self.head
        self.head.next = newnode
        temp.prev = newnode

    def delete_node(self, delnode):
        prevv = delnode.prev
        nextt = delnode.next
        prevv.next = nextt
        nextt.prev = prevv

    def get(self, key: int) -> int:
        if key in self.mp:
            resNode = self.mp[key]
            ans = resNode.val
            del self.mp[key]
            self.delete_node(resNode)
            self.add_node(resNode)
            self.mp[key] = self.head.next
            return ans
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            curr = self.mp[key]
            del self.mp[key]
            self.delete_node(curr)

        if len(self.mp) == self.cap:
            del self.mp[self.tail.prev.key]
            self.delete_node(self.tail.prev)

        self.add_node(self.Node(key, value))
        self.mp[key] = self.head.next