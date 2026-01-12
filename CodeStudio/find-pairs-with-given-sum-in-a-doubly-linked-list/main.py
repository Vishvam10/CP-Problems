class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def findPairs(head: Node, k: int) -> [[int]]:
    ans = []
    mp = set()
    while head:
        target = k - head.data
        if target in mp:
            ans.append([target, head.data])
        else:
            mp.add(head.data)
        head = head.next
    return ans

    # ASSUMING THE LIST IS SORTED, THEN BINARY SEARCH

    # ans = []
    # low, high = head, head
    # while(high.next) :
    #     high = high.next

    # while(low != high and low != high.next) :

    #     if(low.data + high.data == k) :
    #         ans.append([low.data, high.data])
    #         low = low.next
    #         high = high.prev
    #     elif(low.data + high.data > k) :
    #         high = high.prev
    #     else :
    #         low = low.next

    #     if(low == high) :
    #         break

    # return ans
