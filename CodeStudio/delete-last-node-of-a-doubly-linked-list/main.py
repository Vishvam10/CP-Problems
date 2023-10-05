class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Do not change code above.


def deleteLastNode(head: Node) -> Node: 
    temp = head
    if(temp == None or temp.next == None) :
        return None
        
    while(temp.next.next) :
        temp = temp.next

    temp.next = None
    return head