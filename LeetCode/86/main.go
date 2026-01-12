package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func partition(head *ListNode, x int) *ListNode {

	greaterHead, lesserHead := &ListNode{Val: -1, Next: nil}, &ListNode{Val: -1, Next: nil}
	greaterPtr, lesserPtr := greaterHead, lesserHead

	for head != nil {

		if head.Val < x {
			lesserPtr.Next = head
			lesserPtr = lesserPtr.Next
		} else {
			greaterPtr.Next = head
			greaterPtr = greaterPtr.Next
		}

		head = head.Next
	}

	greaterPtr.Next = nil
	lesserPtr.Next = greaterHead.Next

	return lesserHead.Next

}
