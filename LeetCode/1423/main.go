package main

import "fmt"

func maxScore(arr []int, k int) int {
	n := len(arr)

	left, s, totalSum, minSum := 0, 0, 0, 0

	for i := 0; i < n-k; i++ {
		s += arr[i]
		totalSum += arr[i]
	}

	minSum = s

	for right := n - k; right < n; right++ {
		s += arr[right]
		s -= arr[left]
		left++

		minSum = min(minSum, s)
		totalSum += arr[right]
	}

	return totalSum - minSum

}
