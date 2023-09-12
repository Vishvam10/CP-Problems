'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def findIntersection(head1, head2):
    temp1, temp2 = head1, head2
    while(temp1 != temp2) :
        temp1 = temp1.next if temp1 else head2
        temp2 = temp2.next if temp2 else head1
    return temp1