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
  struct Node {
    ListNode *lnode;
    int val;

    Node(ListNode *_lnode, int _val) : lnode(_lnode), val(_val) {}

    bool operator<(const Node &node) const { return val > node.val; }
  };

  ListNode *mergeKLists(vector<ListNode *> &lists) {

    priority_queue<Node> h;

    ListNode *head = new ListNode(-1);
    ListNode *ans = head;

    for (int i = 0; i < lists.size(); i++) {
      if (lists[i] != nullptr) {
        h.push(Node(lists[i], lists[i]->val));
      }
    };

    while (!h.empty()) {

      // the element with the least val
      Node ele = h.top();
      h.pop();

      ListNode *ptr = ele.lnode;
      int val = ele.val;

      head->next = ptr;
      head = head->next;

      if (ptr->next != nullptr) {
        h.push(Node(ptr->next, ptr->next->val));
      }
    }

    return ans->next;
  }
};