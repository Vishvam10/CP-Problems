/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func rightSideView(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	ans := []int{}
	q := []*TreeNode{}
	q = append(q, root)

	for len(q) > 0 {
		sz, visible := len(q), 0
		for i := 0; i < sz; i++ {
			ele := q[0]
			visible = ele.Val
			q = q[1:]
			if ele.Left != nil {
				q = append(q, ele.Left)
			}
			if ele.Right != nil {
				q = append(q, ele.Right)
			}
		}
		ans = append(ans, visible)
	}
	return ans

}