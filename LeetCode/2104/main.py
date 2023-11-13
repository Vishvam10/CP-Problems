from collections import deque

class Solution:
    def subArrayRanges(self, arr: List[int]) -> int:

        def nse_left(arr) :
            n = len(arr)
            res = [-1] * n
            st = deque()

            for i in range(n) :
                
                while(st and arr[i] >= st[-1][0]) :
                    st.pop()

                
                res[i] = st[-1][1] if st else -1
                st.append((arr[i], i))
                    
            return res

        def nse_right(arr) :
            n = len(arr)
            res = [n] * n
            st = deque()

            for i in range(n-1, -1, -1) :
                
                while(st and arr[i] > st[-1][0]) :
                    st.pop()

                res[i] = st[-1][1] if st else n
                st.append((arr[i], i))
                
            return res

        def nge_left(arr) :
            n = len(arr)
            res = [-1] * n
            st = deque()

            for i in range(n) :
                
                while(st and arr[i] <= st[-1][0]) :
                    st.pop()

                res[i] = st[-1][1] if st else -1
                st.append((arr[i], i))
                
            return res

        def nge_right(arr) :
            n = len(arr)
            res = [n] * n
            st = deque()

            for i in range(n-1, -1, -1) :
                
                while(st and arr[i] < st[-1][0]) :
                    st.pop()

                res[i] = st[-1][1] if st else n
                st.append((arr[i], i))
                
            return res

        n = len(arr)
        ans = 0

        left_min = nse_left(arr)
        left_max = nge_left(arr)
        right_min = nse_right(arr)
        right_max = nge_right(arr)

        for i in range(n) :
            is_min = (i - left_min[i]) * (right_min[i] - i)
            is_max = (i - left_max[i]) * (right_max[i] - i)

            ans += (is_max - is_min) * arr[i]

        return abs(ans)