package main

func searchInsert(arr []int, target int) int {

	n := len(arr)
	low, high := 0, n-1

	for low <= high {
		mid := low + (high-low)/2
		if arr[mid] == target {
			return mid
		} else if arr[mid] < target {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}

	return low

}
