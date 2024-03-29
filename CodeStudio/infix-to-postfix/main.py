from collections import deque


def infixToPostfix(s: str) -> str:

    prec = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 0}
    ans = ""
    st = deque()

    for ch in s:

        if (ch == '('):
            st.append(ch)

        elif (ch == ')'):

            while (st[-1] != '('):
                ans += st.pop()

            # Pop the (
            st.pop()

        elif (ch in prec):

            while (st and prec[st[-1]] >= prec[ch]):
                ans += st.pop()

            st.append(ch)

        else:

            ans += ch

    while (st):
        ans += st.pop()

    return ans
