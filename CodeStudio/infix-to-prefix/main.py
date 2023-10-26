from collections import deque

def infixToPostfix(s: str) -> str:
    
    prec = {'+': 1,'-': 1,'*': 2,'/': 2,'^': 3,'(': 0}
    ans = ""
    st = deque()

    for ch in s :

        if(ch == '(') :
            st.append(ch)
        
        elif(ch == ')') :

            while(len(st) > 0 and st[-1] != '(') :
                ans += (st.pop())
            
            # Pop the (
            st.pop()
        
        elif(ch in prec) :

            while(len(st) > 0 and prec[st[-1]] >= prec[ch]) :
                ans += (st.pop())
            
            st.append(ch)
        
        else :
            ans += ch
    
    while(len(st) > 0) :
        ans += (st.pop())

    return ans 


def infixToPrefix(s: str) -> str :

    inf = list(s)
    rev_inf = s[::-1]

    for i in range(len(rev_inf)) :
        if(rev_inf[i] == '(') :
            rev_inf[i] = ')'
        elif(rev_inf[i] == ')') :
            rev_inf[i] = '('
    
    rev_inf = ''.join(rev_inf)
    
    post = infixToPostfix(rev_inf)
    pref = post[::-1]

    return pref

