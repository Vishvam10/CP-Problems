class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
      

        def solve(ind, pref, target):
            if(target == 0 and len(pref) == k): 
                # Copy of pref
                ans.append(pref[:])    
                return 

            for i in range(ind,len(arr)):
                if target < arr[i]:
                    break

                # Set the state
                pref.append(arr[i])     
                
                # Goto next state
                solve(i+1, pref, target - arr[i])  
                
                # Reset the state
                pref.pop()       

        if k > n:   
            return []
        if n > 45:   
            return []
            
        arr = range(1,10)
        ans = []
        solve(0,[],n)
        
        return ans