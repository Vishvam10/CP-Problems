from collections import deque


class Solution:
    def nextGreaterElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [-1] * n
        st = []

        # Copy the array to take care of circular part
        # Hence the 2n - 1

        for i in range(2 * n - 1, -1, -1):
            while st and st[-1] <= arr[i % n]:
                st.pop()

            # We only want the nge's of first n elements
            if i < n:
                if st:
                    ans[i] = st[-1]

            st.append(arr[i % n])

        return ans
