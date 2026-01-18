package 
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func traverse(node *TreeNode, num *int, k int, ans *int) {

    if node == nil {
        return
    }

    traverse(node.Left, num, k, ans)

    (*num) += 1
    if (*num) == k {
        (*ans) = node.Val
        return
    }

    traverse(node.Right, num, k, ans)
}

func kthSmallest(root *TreeNode, k int) int {
    ans, num := 0, 0
    traverse(root, &num, k, &ans)
    return ans
}