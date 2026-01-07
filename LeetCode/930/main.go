func numSubarraysWithSum(arr []int, goal int) int {
	n := len(arr)
	left, sum, ans := 0, 0, 0

	for right := 0; right < n; right++ {

		sum += arr[right]

		for sum > goal {
			sum -= arr[left]
			left++
		}

		ans += (right - left + 1)

	}

	return ans

}