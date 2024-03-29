# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Proof of convergence : Based on difference of length. So, at one point
# they will converge at the intersection node for sure

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tempA, tempB = headA, headB
        while (tempA != tempB):
            tempA = tempA.next if tempA else headB
            tempB = tempB.next if tempB else headA
        return tempA
