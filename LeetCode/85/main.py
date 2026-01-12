from collections import deque


class Solution:
    def maximalRectangle(self, mat: List[List[str]]) -> int:
        n = len(mat)  # no. of rows
        m = len(mat[0])  # no. of cols
        arr = []
        ans = 0

        def get_height(r, c):
            row = list(map(int, mat[r][c:]))
            res = 0
            for x in row:
                if x == 0:
                    break
                res += 1
            return res

        for j in range(m):
            hs = []
            for i in range(n):
                hs.append(get_height(i, j))
            arr.append(hs)

        def largest_rectangle_area(a):
            n = len(a)
            ans = 0
            st = deque()
            lefts = [0] * n
            rights = [0] * n

            for i in range(n):
                while len(st) > 0 and a[i] <= st[-1][0]:
                    st.pop()
                lefts[i] = 0 if len(st) == 0 else st[-1][1] + 1
                st.append((a[i], i))

            while len(st) > 0:
                st.pop()

            for i in range(n - 1, -1, -1):
                while len(st) > 0 and a[i] <= st[-1][0]:
                    st.pop()

                rights[i] = (n - 1) if len(st) == 0 else st[-1][1] - 1
                st.append((a[i], i))

            for i in range(n):
                ans = max(ans, a[i] * (rights[i] - lefts[i] + 1))

            return ans

        for i, a in enumerate(arr):
            ans = max(ans, largest_rectangle_area(a))

        return ans
