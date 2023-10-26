from collections import deque

def prefixToInfixConversion(s: str) -> str:
    
    s = s[::-1]
    st = deque()

    for ch in s :

        if(ch in '+-*/') :
            op1 = st.pop()
            op2 = st.pop()
            op = ch
            fstr = '({}{}{})'.format(op1, op, op2)
            st.append(fstr)
        else :
           st.append(ch)

    return st[0]
    
            









