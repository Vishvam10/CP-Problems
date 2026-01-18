package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func solve(node *TreeNode, head **TreeNode) {
	if node == nil {
		return
	}

	(*head).Right = node
	(*head).Left = nil

	left, right := node.Left, node.Right

	(*head) = (*head).Right

	solve(left, head)
	solve(right, head)
}

func flatten(root *TreeNode) {
	dummy := &TreeNode{}
	head := dummy
	solve(root, &head)
}
