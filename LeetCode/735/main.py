class Solution:
    def asteroidCollision(self, arr: List[int]) -> List[int]:
        
        n = len(arr)
        ans = []

        i = 0

        while(i < n) :
            
            if(len(ans) == 0) :
                ans.append(arr[i])
            else :
                prev, cur = ans[-1], arr[i]

                if(prev < 0 or cur > 0) :
                    ans.append(cur)
                else :
                    if(prev == abs(cur)) :
                        ans.pop()
                    elif(prev < abs(cur)):
                        ans.pop()
                        i -= 1
                
            i += 1

        return ans

