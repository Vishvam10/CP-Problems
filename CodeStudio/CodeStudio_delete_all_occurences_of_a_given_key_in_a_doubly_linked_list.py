class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def deleteAllOccurrences(head: Node, k: int) -> Node:
    
    temp = head
    while(temp) :
        nxt = temp.next
        if(temp.data == k) :
            if(temp.prev) :
                # Body node
                if(temp.next) :
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                # Tail node
                else :
                    temp.prev.next = None
            else :
                # Head node
                if(temp.next) :
                    temp.next.prev = None
                    head = nxt
                    
                # Detached node
                else :
                    temp = None
                    head = nxt
        
        temp = nxt
    return head

        