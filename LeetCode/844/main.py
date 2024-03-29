class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st1 = []
        st2 = []
        for ch in s:
            if (ch == "#"):
                if (len(st1) != 0):
                    st1.pop()
            else:
                st1.append(ch)
        for ch in t:
            if (ch == "#"):
                if (len(st2) != 0):
                    st2.pop()
            else:
                st2.append(ch)

        while (len(st1) > 0 and len(st2) > 0):
            a = st1.pop()
            b = st2.pop()
            if (a != b):
                return False
        if (st1 or st2):
            return False
        return True
