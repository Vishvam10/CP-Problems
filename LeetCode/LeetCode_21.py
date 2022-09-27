# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        dummy = new_head
        while list1 and list2:               
            if list1.val < list2.val:
                new_head.next = list1
                list1, new_head = list1.next, list1
            else:
                new_head.next = list2
                list2, new_head = list2.next, list2
                
        if list1 or list2:
            new_head.next = list1 if list1 else list2
            
        return dummy.next
        
