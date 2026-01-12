package main

import "fmt"

// Count binary subarray with sum k basically. So, use atMost thing
// and use % 2 as condition to make it binary

func atMost(arr []int, k int) int {

	if k < 0 {
		return 0
	}

	n := len(arr)
	left, oddCount, totalSubarrays := 0, 0, 0

	for right := 0; right < n; right++ {

		if arr[right]%2 == 1 {
			oddCount++
		}

		for oddCount > k {
			if arr[left]%2 == 1 {
				oddCount--
			}
			left++
		}

		totalSubarrays += (right - left + 1)
	}

	return totalSubarrays

}

func numberOfSubarrays(arr []int, k int) int {
	return atMost(arr, k) - atMost(arr, k-1)
}
