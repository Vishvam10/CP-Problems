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
  ListNode *removeElements(ListNode *head, int val) {
    ListNode *dummy = new ListNode(-1, head);
    ListNode *temp = dummy;

    while (temp && temp->next) {
      if (temp->next && temp->next->val == val) {
        ListNode *ptr = temp->next;
        while (ptr && ptr->val == val) {
          ptr = ptr->next;
        }
        temp->next = ptr;
      }
      temp = temp->next;
    }

    return dummy->next;
  }
};