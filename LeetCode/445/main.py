"""
DIFFICULTY : medium
TAGS : linked list, stack, math
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        st1, st2 = [], []
        carry = 0
        head = None
        while (l1):
            st1.append(l1.val)
            l1 = l1.next
        while (l2):
            st2.append(l2.val)
            l2 = l2.next

        while (st1 or st2 or carry):
            val1, val2 = 0, 0
            # val1 and val2 being 0 takes care of cases :
            # 1. Stack 1 is empty but have carry
            # 2. Stack 2 is empty but have carry
            # 3. Both of the stacks are empty but have carry
            if (st1):
                val1 = st1.pop()
            else:
                val1 = 0
            if (st2):
                val2 = st2.pop()
            else:
                val2 = 0

            carry, digit = divmod(val1 + val2 + carry, 10)

            # ADDING FROM START
            new_node = ListNode(digit)
            new_node.next = head
            head = new_node

        return head
