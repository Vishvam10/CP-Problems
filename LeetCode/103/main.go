package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func rev(s *[]int) {
	for i, j := 0, len(*s)-1; i < j; i, j = i+1, j-1 {
		(*s)[i], (*s)[j] = (*s)[j], (*s)[i]
	}
}

func zigzagLevelOrder(root *TreeNode) [][]int {

	if root == nil {
		return [][]int{}
	}

	ans := [][]int{}
	q := []*TreeNode{root}

	flag := false

	for len(q) != 0 {

		sz := len(q)
		levels := []int{}

		for i := 0; i < sz; i++ {

			node := q[0]
			q = q[1:]
			levels = append(levels, node.Val)

			if node.Left != nil {
				q = append(q, node.Left)
			}
			if node.Right != nil {
				q = append(q, node.Right)
			}

		}

		if flag {
			rev(&levels)
		}
		ans = append(ans, levels)
		flag = !flag
	}

	return ans
}
