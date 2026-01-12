package main

func lengthOfLongestSubstring(s string) int {
	n := len(s)
	vis := [256]bool{false}
	left, ans := 0, 0

	for right := 0; right < n; right++ {
		for vis[s[right]] {
			vis[s[left]] = false
			left++
		}
		vis[s[right]] = true
		ans = max(ans, right-left+1)
	}

	return ans
}
