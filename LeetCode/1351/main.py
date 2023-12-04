class Solution:
    def countNegatives(self, arr: List[List[int]]) -> int:

        n = len(arr)    
        m = len(arr[0])
        row, col, ans = 0, m - 1, 0

        while(row <= n - 1 and col >= 0) :
            if(arr[row][col] < 0) :
                ans += (n - row)
                col -= 1
            else :
                row += 1
        
        return ans
    