package 
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func solve(node *TreeNode) *TreeNode {
    if node == nil {
        return nil
    }

    left := solve(node.Left)
    right := solve(node.Right)

    if left != nil {
        left.Right = node.Right
        node.Right = node.Left
        node.Left = nil
    }

    if right != nil {
        return right
    }

    if left != nil {
        return left
    }

    return node

}

func flatten(root *TreeNode)  {
    root = solve(root)
}