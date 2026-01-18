package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func check(node *TreeNode, ans *bool) {
	if node == nil || !(*ans) {
		return
	}

	if (node.Left != nil && node.Val <= node.Left.Val) ||
		(node.Right != nil && node.Val >= node.Right.Val) {
		*ans = false
		return
	}

	check(node.Left, ans)
	check(node.Right, ans)

}

func isValidBST(root *TreeNode) bool {
	ans := true
	check(root, &ans)
	return ans
}
