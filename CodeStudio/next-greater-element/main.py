from typing import List
from collections import deque, defaultdict


def nextGreaterElement(arr: List[int], n: int) -> List[int]:
    # Write your code here.
    st = deque()
    ans = [-1] * n

    st.append(arr[n-1])
    ans[n-1] = -1

    for i in range(n-2, -1, -1):

        if (arr[i] < st[-1]):
            ans[i] = st[-1]
            st.append(arr[i])
        else:
            while (len(st) > 0 and arr[i] >= st[-1]):
                st.pop()
            ans[i] = st[-1] if len(st) > 0 else -1
            st.append(arr[i])

    return ans
