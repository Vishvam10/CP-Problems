from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        st = deque()

        for ch in s:
            if (ch in '([{'):
                st.append(ch)
            else:
                if (
                    (len(st) > 0) and
                    ((st[-1] == '(' and ch == ')') or
                     (st[-1] == '{' and ch == '}') or
                     (st[-1] == '[' and ch == ']'))
                ):
                    st.pop()
                else:
                    return False

        return True if (len(st) == 0) else False
