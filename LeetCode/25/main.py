# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def rev(start, end):
            prev = None
            cur = start
            while (cur != end):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev

        def pl(node):
            while (node):
                print(node.val, ' -> ', end='')
                node = node.next
            return

        dummy = ListNode(-1)
        ans = dummy

        temp = head
        while (temp):
            start = temp
            flag = True
            c = 0
            while (c < k and flag):
                if (temp):
                    temp = temp.next
                    c += 1
                else:
                    flag = False
            end = temp

            if (c == k):
                rhead = rev(start, end)
                dummy.next = rhead
                for _ in range(k):
                    dummy = dummy.next
            else:
                # print('start, dummy, end : ', start, dummy, end)
                dummy.next = start
                dummy = dummy.next

        # pl(ans.next)

        return ans.next
