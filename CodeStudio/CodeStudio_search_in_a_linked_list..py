'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def searchInLinkedList(head, k):  
    while(head) :
        if(head.data == k) :
            return 1
        head = head.next
    return 0