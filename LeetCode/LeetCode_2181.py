"""
DIFFICULTY : medium
TAGS : linked list, simulation
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        curr = start.next
        s = 0
        while(curr) :
            if(curr.val == 0) :
                head.next = ListNode(s)
                head = head.next
                s = 0
            else :
                s += curr.val;
            curr = curr.next;
        return start.next;
                