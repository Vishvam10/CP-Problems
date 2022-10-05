class Solution:
    # OPTION 1 :
    # Rob the ith house, then can't rob the previous house (i-1)
    # => money = everything from (i-2)th house + money from current house
    
    # OPTION 2 :
    # Don't rob the ith house, then we can rob the previous house (i-1)
    # => money = everything from (i-1)th house
    
    # ANSWER = max(OPTION1, OPTION2). Continue this till i=n
    
    # Here, instead of starting with i, we start with (i+1) 
    # which nicely makes the other 2 terms i and (i-1) respectively
    
    def rob(self, arr: List[int]) -> int:
        n = len(arr)
        if(n == 0) :
            return 0
        # ans = [None]*(n+1)
        # ans[0] = 0
        # ans[1] = arr[0]
        # for i in range(1, n) :
        #     ans[i+1] = max(ans[i-1] + arr[i], ans[i])
        # return ans[n]
    
        # FURTHER OPTIMIZATION : Clearly, at a time, we need
        # only 2 variables : ans[i] and ans[i-1]
        
        a, b = 0, 0
        for i in range(n) :
            temp = a
            a = max(a, b+arr[i])
            b = temp
        return a
    
        
            
            
        
        