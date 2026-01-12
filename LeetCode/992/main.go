package main

func atMost(arr []int, k int) int {
	n := len(arr)

	left, right, cnt, ans := 0, 0, 0, 0
	mp := make(map[int]int)

	for right < n {

		if mp[arr[right]] == 0 {
			cnt++
		}
		mp[arr[right]]++

		for cnt > k {
			mp[arr[left]]--
			if mp[arr[left]] == 0 {
				cnt--
			}
			left++
		}

		ans += right - left + 1
		right++

	}

	return ans
}

func subarraysWithKDistinct(nums []int, k int) int {
	return atMost(nums, k) - atMost(nums, k-1)
}
