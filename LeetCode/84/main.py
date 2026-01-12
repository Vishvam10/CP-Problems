from collections import deque


class Solution:
    # ans = max(ans, (rights[i] - lefts[i] + 1) * arr[i])
    # lefts and rights => nse to left and right for each element
    def largestRectangleArea(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        lefts = [0] * n  # next smallest to left for each element
        rights = [0] * n  # next smallest to right for each element

        st = deque()

        for i in range(n):
            while len(st) > 0 and arr[i] <= st[-1][0]:
                st.pop()

            lefts[i] = 0 if len(st) == 0 else st[-1][1] + 1
            st.append((arr[i], i))

        while len(st) > 0:
            st.pop()

        for i in range(n - 1, -1, -1):
            while len(st) > 0 and arr[i] <= st[-1][0]:
                st.pop()

            rights[i] = (n - 1) if len(st) == 0 else st[-1][1] - 1
            st.append((arr[i], i))

        for i in range(n):
            ans = max(ans, (rights[i] - lefts[i] + 1) * arr[i])

        return ans
