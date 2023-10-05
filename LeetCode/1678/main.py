"""
DIFFICULTY : easy
TAGS : string
"""
class Solution:
    def interpret(self, s: str) -> str:
        """
            ALTERNATE SOLUTION (FASTER): 
            
            s = s.replace("()", "o")
            s = s.replace("(", "")
            s = s.replace(")", "")
            return s

        """
        res = ""
        st = []

        for ch in s :
            if(ch != "G" and ch != ")") :
                st.append(ch)
            elif(ch == ")") :
                top = st[-1]
                if(top == "(") :
                    res += "o"
                    st.pop()
                elif(top == "l") :
                    res += "al"
                    st.pop()
                    st.pop()
            elif(ch == "G") :
                res += "G"
        
        return res
