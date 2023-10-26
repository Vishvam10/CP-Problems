from collections import deque

def postToInfix(s: str) -> str:
    
    ans = ""
    st = deque()

    for ch in s :

        if(ch in '+-*/^') :
            op1 = st.pop()
            op2 = st.pop()
            op = ch
            fstr = '({}{}{})'.format(op2, op, op1)
            st.append(fstr)
        
        else :
            st.append(ch)
    
    ans = st.pop()

    return ans










