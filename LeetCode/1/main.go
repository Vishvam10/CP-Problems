func twoSum(nums []int, target int) []int {
	n := len(nums)
	mp := map[int]int{}

	for i := 0; i < n; i++ {
		val := target - nums[i]
		if ind, exists := mp[val]; exists {
			return []int{ind, i}
		}
		mp[nums[i]] = i
	}

	return []int{}

}