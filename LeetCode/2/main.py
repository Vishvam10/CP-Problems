# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def p(head):
    while (head):
        print(head.val, '-> ', end='')
        head = head.next
    return


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(-1)
        start = ans
        carry = 0
        while (l1 and l2):
            s = (l1.val + l2.val + carry)
            temp = ListNode(s % 10)

            carry = 1 if s > 9 else 0

            ans.next = temp
            l1, l2, ans = l1.next, l2.next, ans.next

        if (l1):
            while (carry == 1 and l1):
                s = (l1.val + carry)
                temp = ListNode(s % 10)
                carry = 1 if s > 9 else 0
                ans.next = temp
                l1, ans = l1.next, ans.next
            ans.next = l1

        if (l2):
            while (carry == 1 and l2):
                s = (l2.val + carry)
                temp = ListNode(s % 10)
                carry = 1 if s > 9 else 0
                ans.next = temp
                l2, ans = l2.next, ans.next
            ans.next = l2

        if (carry == 1):
            ans.next = ListNode(1)

        # p(start.next)
        return start.next
