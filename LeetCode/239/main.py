from collections import deque

class Solution:
  
    def maxSlidingWindow(self, arr: List[int], ws: int) -> List[int]:
     
        n = len(arr)
        dq = deque()
        ans = []
        left, right = 0, 0

        while(right < n) :

            while(dq and arr[right] > arr[dq[-1]]) :
                dq.pop()
            
            dq.append(right)

            # remove elements out of the window
            if(left > dq[0]) :
                dq.popleft()

            # if window size is reached
            if(right >= (ws - 1)) :
                ans.append(arr[dq[0]])
                left += 1
            
            right += 1
        
        return ans

