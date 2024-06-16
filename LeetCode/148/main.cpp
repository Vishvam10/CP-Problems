/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
  typedef ListNode ln;

  ln *merge(ln *head1, ln *head2) {
    ln *dummy = new ln(-1);
    ln *p3 = dummy;

    while (head1 != nullptr && head2 != nullptr) {
      if (head1->val < head2->val) {
        p3->next = head1;
        head1 = head1->next;
      } else {
        p3->next = head2;
        head2 = head2->next;
      }
      p3 = p3->next;
    }

    if (head1 != nullptr) {
      p3->next = head1;
    }

    if (head2 != nullptr) {
      p3->next = head2;
    }

    ln *mergedHead = dummy->next;
    delete dummy;

    return mergedHead;
  }

  ln *split(ln *head) {

    ln *slow = head;
    ln *fast = head->next;

    while (fast != nullptr) {
      fast = fast->next;
      if (fast != nullptr) {
        slow = slow->next;
        fast = fast->next;
      }
    }

    ln *mid = slow->next;

    // we must break the list here else
    // it will go into an inf loop
    slow->next = nullptr;

    // mid point
    return mid;
  }

  ln *sortList(ln *node) {

    if (node == nullptr || node->next == nullptr) {
      return node;
    }

    ln *mid = split(node);
    ln *left = sortList(node);
    ln *right = sortList(mid);

    return merge(left, right);
  }
};