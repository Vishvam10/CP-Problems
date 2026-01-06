import (
    "math"
)

func maxSubArray(nums []int) int {

    n := len(nums)
    curSum, ans := 0, math.MinInt

    for i := 0; i < n; i++ {

        curSum += nums[i]
        ans = max(curSum, ans)

        if (curSum < 0) {
            curSum = 0
        }
    }

    return ans
    
}