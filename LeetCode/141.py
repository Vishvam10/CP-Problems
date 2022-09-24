"""
DIFFICULTY : easy
TAGS : hash table, linked list, two pointers
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Instead of checking the boundary condition i.e.
    # if the list ends without a cycle (internally, pos = -1, 
    # as mentioned in the question), we can wrap the algorithm
    # in a try-except block and return False when slow.next 
    # or fast.next.next does not exist
    
    
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try :
            slow = head
            fast = head.next
            while(slow is not fast) :
                slow = slow.next
                fast = fast.next.next
            return True
        except :
            return False