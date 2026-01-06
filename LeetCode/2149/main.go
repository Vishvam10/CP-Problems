func rearrangeArray(nums []int) []int {
    n := len(nums)
	result := make([]int, n)
	posI, negI := 0, 1
	for i := 0; i < n; i++ {
		if nums[i] > 0 {
			if posI < n {
				result[posI] = nums[i]
				posI += 2
			}
		} else {
			if negI < n {
				result[negI] = nums[i]
				negI += 2
			}
		}
	}
	return result
}