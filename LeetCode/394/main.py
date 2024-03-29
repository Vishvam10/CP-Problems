class Solution:
    # THE NUMBER CAN HAVE MORE THAN ONE DIGITS. So, we can either
    # do num = num * 10 + int(s[it]) (num is converted to an integer)
    # and reset num if ch == "[" or take num as a string and do
    # num += ch and reset num if ch == "["
    def decodeString(self, s: str) -> str:
        st = []
        st.append(["", 1])
        num = ""
        for ch in s:
            if (ch.isdigit()):
                num += ch
            elif (ch == "["):
                st.append(["", int(num)])
                num = ""
            elif (ch == "]"):
                string, n = st.pop()
                c = string*n
                # CONCATENATING THE RESULTING STRING INTO THE LAST ELEMENT
                # OF THE STACK ===> CRUX OF THE PROBLEM
                st[-1][0] += c
            else:
                st[-1][0] += ch
        return st[0][0]
