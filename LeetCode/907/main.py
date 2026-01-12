from collections import deque


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)

        def nse_left(arr):
            n = len(arr)
            res = [0] * n
            st = deque()

            for i in range(n):
                while st and arr[i] <= arr[st[-1]]:
                    st.pop()

                res[i] = st[-1] if st else 0
                st.append(i)

            return res

        def nse_right(arr):
            n = len(arr)
            res = [0] * n
            st = deque()

            for i in range(n - 1, -1, -1):
                while st and arr[i] < arr[st[-1]]:
                    st.pop()

                res[i] = st[-1] if st else (n - 1)
                st.append(i)

            return res

        lefts = nse_left(arr)
        rights = nse_right(arr)
        ans = 0

        for i in range(n):
            l = abs(i - lefts[i])
            r = abs(i - rights[i])
            ans += arr[i] * l * r

        return ans
