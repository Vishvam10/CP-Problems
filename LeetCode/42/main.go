package main

func trap(arr []int) int {

	n := len(arr)

	if n == 0 {
		return 0
	}

	ans := 0

	lefts, rights := make([]int, n), make([]int, n)
	lefts[0], rights[n-1] = arr[0], arr[n-1]

	for i := 1; i < n; i++ {
		lefts[i] = max(lefts[i-1], arr[i])
	}

	for i := n - 2; i >= 0; i-- {
		rights[i] = max(rights[i+1], arr[i])
	}

	for i := 0; i < n; i++ {
		h := min(lefts[i], rights[i]) - arr[i]
		ans += h
	}

	return ans

}
