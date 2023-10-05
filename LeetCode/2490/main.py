class Solution:
    def isCircularSentence(self, s: str) -> bool:
        arr = s.split(" ")
        start = arr[0]
        end = arr[len(arr) - 1]
        
        if(len(arr) == 1) :
            if(start[0] == start[len(start) - 1]) :
                return True
            return False

        if(start[0] != end[len(end)-1]) :
            return False
        
        for i in range(1, len(arr)) :
            curr = arr[i]
            prev = arr[i-1]
            
            prev_end = prev[len(prev) - 1]
            curr_start = curr[0]
            
            if(curr_start != prev_end) :
                return False
        
        
        return True