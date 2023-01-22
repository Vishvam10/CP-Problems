"""
DIFFICULTY : easy
TAGS : array
"""
class Solution:
    def summaryRanges(self, arr: List[int]) -> List[str]:
        left = 0
        right = 0
        ans = []
        while(left < len(arr) and right < len(arr)) :
            if(
                (right + 1 < len(arr)) and 
                (arr[right] + 1 == arr[right+1])
            ) :
                right += 1
            else :
                if(left == right) :
                    ans.append(str(arr[left]))
                    left += 1
                    right += 1
                else :
                    ans.append(str(arr[left]) + "->" + str(arr[right]))
                    left = right + 1
                    right += 1

        return ans
                
