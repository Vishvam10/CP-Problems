package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func preorder(node *TreeNode, ans *[]int) {

	if node == nil {
		return
	}

	*ans = append(*ans, node.Val)
	preorder(node.Left, ans)
	preorder(node.Right, ans)
}

func preorderTraversal(root *TreeNode) []int {
	ans := []int{}
	preorder(root, &ans)
	return ans
}
