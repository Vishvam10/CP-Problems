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
  ListNode *mergeTwoLists(ListNode *head1, ListNode *head2) {
    if (head1 == NULL) {
      return head2;
    }
    if (head2 == NULL) {
      return head1;
    }

    ListNode *res = new ListNode(-1);
    ListNode *ans = res;
    ListNode *temp1 = head1;
    ListNode *temp2 = head2;

    while (temp1 != NULL && temp2 != NULL) {
      if (temp1->val < temp2->val) {
        res->next = temp1;
        temp1 = temp1->next;
      } else {
        res->next = temp2;
        temp2 = temp2->next;
      }
      res = res->next;
    }

    if (temp1 != NULL) {
      res->next = temp1;
    }

    if (temp2 != NULL) {
      res->next = temp2;
    }

    return ans->next;
  }
};