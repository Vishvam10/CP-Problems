class Solution:
    # EASY SOLUTION : Square all elements and sort the array
    # EFFICIENT SOLUTION : Use 2 pointers + 1 write pointer
    def sortedSquares(self, arr: List[int]) -> List[int]:
        ans = [None]*len(arr)
        a, b, write_ptr = 0, len(arr) - 1, len(arr) - 1
        left_sq, right_sq = arr[a]*arr[a], arr[b]*arr[b]
        while(write_ptr >= 0) :
            if(left_sq > right_sq) :
                ans[write_ptr] = arr[a] * arr[a]
                a += 1
                left_sq = arr[a] * arr[a]
            else :
                ans[write_ptr] = arr[b] * arr[b]
                b -= 1
                right_sq = arr[b] * arr[b]
            write_ptr -= 1
        
        return ans
                
            