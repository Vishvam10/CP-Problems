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
  ListNode *reverse(ListNode *node) {
    ListNode *curr = node;
    ListNode *prev = NULL;
    while (curr) {
      ListNode *nxt = curr->next;
      curr->next = prev;
      prev = curr;
      curr = nxt;
    }
    return prev;
  }
  bool isPalindrome(ListNode *head) {
    ListNode *ptr1 = head;
    ListNode *ptr2 = head;

    while (ptr2 && ptr2->next) {
      ptr1 = ptr1->next;
      ptr2 = ptr2->next->next;
    }

    ptr1 = reverse(ptr1);
    ptr2 = head;

    while (ptr1) {
      if (ptr1->val != ptr2->val) {
        return false;
      }
      ptr1 = ptr1->next;
      ptr2 = ptr2->next;
    }

    return true;
  }
};