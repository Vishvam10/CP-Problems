package main

func atMost(arr []int, goal int) int {
	if goal < 0 {
		return 0
	}

	left, sum, ans := 0, 0, 0

	for right := 0; right < len(arr); right++ {
		sum += arr[right]

		for sum > goal {
			sum -= arr[left]
			left++
		}

		ans += right - left + 1
	}

	return ans
}

func numSubarraysWithSum(arr []int, goal int) int {
	return atMost(arr, goal) - atMost(arr, goal-1)
}
