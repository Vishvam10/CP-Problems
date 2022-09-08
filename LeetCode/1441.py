class Solution:
    # NOTE : i is from 1, target[-1] + 1 and
    # not from 1 to len(target)
    
    # Also, we don't need to explicitly keep
    # track of the stack as the question does
    # not ask us to do so
    
    def buildArray(self, target: List[int], n: int) -> List[str]:
        cur = 0
        ans = []
        for i in range(1, target[-1] +1):
            ans.append("Push")
            if i != target[cur]:
                ans.append("Pop")
            else:
                cur +=1
        return ans