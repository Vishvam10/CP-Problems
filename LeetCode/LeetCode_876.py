# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:	
        n = 0
        temp = head
        while(temp) :
            temp = temp.next
            n += 1
        n = n // 2
        i = 0
        temp = head
        print(n)
        while(i < n) :
            temp = temp.next
            i += 1
        return temp