func maxProfit(arr []int) int {
	n := len(arr)

	if n == 0 {
		return 0
	}

	minPrice := arr[0]
	ans := 0

	for i := 0; i < n; i++ {
		if arr[i] <= minPrice {
			minPrice = arr[i]
		} else if arr[i]-minPrice > ans {
			ans = arr[i] - minPrice
		}
	}

	return ans

}