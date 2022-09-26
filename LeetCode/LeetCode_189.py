class Solution:
    # k rotations affect the last k elements
    # So, the answer is return nums[-k:] + num[:K]
    # But we need to do this in place
    
    # Use REVERSE :
    # arr = [1,2,3,4,5,6,7]
    # p1 = [1,2,3,4] and p2 = [5,6,7]
    # reverse(p1) and reverse(p2) in arr itself
    # and finally, reverse(arr)
    
    # Also, the cicular relation is :
    # new_arr[(i+k)%n] = arr_copy[i]
    
    # where arr_copy = arr.copy()
    def reverse (self, nums, i, j) : 
        l = i
        r = j
        
        while l < r:
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            
            l += 1
            r -= 1
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(arr, l, r) :
            while(l <= r) :
                temp = arr[l]
                arr[l] = arr[r]
                arr[r] = temp
                l += 1
                r -= 1

        n = len(nums)
        k = k % n
        if(k < 0) :
            k += len(nums)
            
        self.reverse(nums, 0, n-k-1)
        self.reverse(nums, n-k, n-1)
        self.reverse(nums, 0, n-1)
        