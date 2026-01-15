package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func calc(node *TreeNode, ans *int) int {

	if node == nil {
		return 0
	}

	// max(0, x) to include the case of NOT including that child
	left := max(0, calc(node.Left, ans))
	right := max(0, calc(node.Right, ans))
	sum := node.Val + left + right

	*ans = max(*ans, sum)

	return node.Val + max(left, right)
}

func maxPathSum(root *TreeNode) int {
	ans := math.MinInt
	calc(root, &ans)
	return ans
}
