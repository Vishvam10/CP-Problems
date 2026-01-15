package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func check(node *TreeNode, ans *int) int {
	if node == nil {
		return 0
	}
	left := check(node.Left, ans)
	right := check(node.Right, ans)
	*ans = max(*ans, left+right)
	return 1 + max(left, right)
}

func diameterOfBinaryTree(root *TreeNode) int {
	ans := 0
	check(root, &ans)
	return ans
}
