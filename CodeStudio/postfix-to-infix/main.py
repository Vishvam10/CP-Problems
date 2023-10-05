from collections import deque

def postToInfix(s: str) -> str:
    
    st = deque()
    for ch in s : 
        if(ch not in '+-*/') :
            st.append(ch)
        else :
            op1 = st.pop()      
            op = ch
            op2 = st.pop()      
            fstr = '({}{}{})'.format(op2, op, op1)
            st.append(fstr)
          
    return st.pop()
            