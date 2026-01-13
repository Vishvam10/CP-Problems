package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func traverse(node *TreeNode, ans *[]int) {

	if node == nil {
		return
	}

	traverse(node.Left, ans)
	*ans = append(*ans, node.Val)
	traverse(node.Right, ans)
}

func inorderTraversal(root *TreeNode) []int {
	ans := []int{}
	traverse(root, &ans)
	return ans
}
