"""
DIFFICULTY : medium
TAGS : array, two pointers, simulation
"""

class Solution:
    def rearrangeArray(self, arr: List[int]) -> List[int]:
        pos = []
        neg = []
        ans = []
        for i in range(len(arr)) :
            if(arr[i] > 0) :
                pos.append(arr[i])
            else :
                neg.append(arr[i])
                
        for i in range(len(pos)) :
            ans.append(pos[i])
            ans.append(neg[i])
        
        return ans
        
# ALTERNATE SOLUTION

class Solution:
    """
    result[0] : calculate by traversing all elements
    
    for result[i=1 to n]
    result[i] = result[i-1] - ahead + behind
    ahead = no of elements with value '1' at index >= i
    behind = no of elements with value '1' at index < i
    """
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        behind = 0
        ahead = 0
        result = [0 for i in range(n)]
        # First calculate result at 0th index and count ahead
        for i in range(n):
            if boxes[i] == '1':
                result[0] += i
                ahead += 1
        # Update behind and ahead if first element is 1
        if boxes[0] == '1':
            behind += 1
            ahead -= 1
        # Calculate result using the previous one
        for i in range(1, n):
            result[i] = result[i-1] - ahead + behind
            if boxes[i] == '1':
                ahead -= 1
                behind += 1
        return result