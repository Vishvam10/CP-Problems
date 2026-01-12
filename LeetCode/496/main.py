from collections import deque, defaultdict


class Solution:
    # Use stack to keep track of elements that are smaller
    # than the one present on top of the stack
    def nextGreaterElement(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n = len(arr2)
        st = deque()
        mp = defaultdict(int)
        ans = []

        st.append(arr2[n - 1])
        mp[arr2[n - 1]] = -1

        for i in range(n - 2, -1, -1):
            if arr2[i] < st[-1]:
                mp[arr2[i]] = st[-1]
                st.append(arr2[i])
            else:
                while len(st) > 0 and arr2[i] >= st[-1]:
                    st.pop()

                mp[arr2[i]] = st[-1] if len(st) > 0 else -1
                st.append(arr2[i])

        for x in arr1:
            ans.append(mp[x])

        return ans
