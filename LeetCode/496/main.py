class Solution:
    # Use stack to keep track of elements that are smaller
    # than the one present on top of the stack
    def nextGreaterElement(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mp = {}
        st = []
        ans = []
        for x in arr2 :
            if(len(st) == 0) :
                st.append(x)
            elif(st[-1] >= x) :
                st.append(x)
            else :
                while(st and st[-1] < x) :
                    mp[st.pop()] = x
                st.append(x)
        
        for x in arr1 :
            if(x in mp) :
                ans.append(mp[x])
            else :
                ans.append(-1)
        return ans
             
        