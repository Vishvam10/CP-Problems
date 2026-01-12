package main

func longestOnes(nums []int, k int) int {
	n := len(nums)
	left, zcnt, ans := 0, 0, 0

	for right := 0; right < n; right++ {

		if nums[right] == 0 {
			zcnt++
		}

		for zcnt > k {
			if nums[left] == 0 {
				zcnt--
			}
			left++
		}

		ans = max(ans, right-left+1)
	}

	return ans

}
