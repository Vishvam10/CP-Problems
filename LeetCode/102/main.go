package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode) [][]int {

	if root == nil {
		return [][]int{}
	}

	ans := [][]int{}

	q := []*TreeNode{root}

	for len(q) != 0 {
		size := len(q)
		level := []int{}
		for i := 0; i < size; i++ {
			node := q[0]
			level = append(level, node.Val)
			q = q[1:]

			if node.Left != nil {
				q = append(q, node.Left)
			}
			if node.Right != nil {
				q = append(q, node.Right)
			}
		}
		ans = append(ans, level)
	}
	return ans
}
