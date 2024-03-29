"""
DIFFICULTY : medium
TAGS : string, stack
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        for p in path.split("/"):
            if p == "..":
                if st:
                    st.pop()
            elif p and p != ".":
                st.append(p)
        return "/" + "/".join(st)
