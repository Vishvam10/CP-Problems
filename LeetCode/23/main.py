"""
DIFFICULTY : hard
TAGS : linked list, divide and conquer, heap, merge sort
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# IDEA : Merge 2 sorted lists but do it on the whole array
# by recursively dividing it


class Solution:
    # Divide and conquer : Merge the consequent linked
    # lists in the given array and STORE THE RESULT IN
    # THE ARRAY ITSELF BY OVERWRITING IT

    def mergeKLists(self, arr: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1, l2):
            new_head = ListNode()
            dummy = new_head
            while l1 and l2:
                if l1.val < l2.val:
                    new_head.next = l1
                    l1, new_head = l1.next, l1
                else:
                    new_head.next = l2
                    l2, new_head = l2.next, l2

            if l1 or l2:
                new_head.next = l1 if l1 else l2

            return dummy.next

        # ITERATIVE DIVIDE AND CONQUER
        n = len(arr)
        interval = 1
        while (interval < n):
            for i in range(0, n - interval, interval * 2):
                arr[i] = merge(arr[i], arr[i+interval])
            interval *= 2

        if (n > 0):
            return arr[0]
        return None
