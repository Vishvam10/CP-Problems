class Solution:
    def evalRPN(self, arr: List[str]) -> int:

        st = []

        for s in arr:
            if len(s) == 1 and s in '+-*/':
                b = st.pop()
                a = st.pop()

                if (s == '+'):
                    st.append(a + b)
                elif (s == '-'):
                    st.append(a - b)
                elif (s == '*'):
                    st.append(a * b)
                elif (s == '/'):
                    st.append(int(a / b))

            else:
                st.append(int(s))

        return st.pop()
