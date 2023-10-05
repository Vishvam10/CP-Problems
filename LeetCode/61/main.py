# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def pl(node) :
            while(node) :
                print(node.val, ' -> ', end='')
                node = node.next
            return

        if(head == None) : 
            return None

        temp, temp1 = head, head
        n = 1
        while(temp.next) :
            n += 1
            temp = temp.next 
        k %= n

        # Make it cyclic
        temp.next = head 
        for _ in range(n-k-1) :
            temp1 = temp1.next
        head = temp1.next
        temp1.next = None

        return head

