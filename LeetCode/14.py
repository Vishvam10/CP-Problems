class Solution:
    # Sort the array and compare the first 
    # and last elements. Notice that 
    # len(first) <= len(last) 
    def longestCommonPrefix(self, arr: List[str]) -> str:
        ans = ""
        arr.sort()
        first = arr[0]
        last = arr[-1]
        
        for i in range(len(first)) :
            if(first[i] == last[i]) :
                ans += first[i]
            else :
                break
        return ans