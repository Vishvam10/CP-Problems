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
    ListNode* removeNthFromEnd(ListNode* head, int n) {

        if(head->next == nullptr) {
            return nullptr;
        }

        ListNode* temp = head;
        int i = 0, len = 0;
        
        while(temp != nullptr) {
            temp = temp->next;
            len++;
        }

        if(n == len) {
            ListNode* ans = head->next;
            head = nullptr;
            return ans;
        }

        temp = head;    
        while(temp != nullptr) {
            if(i == len - n - 1) {
                if(temp->next != nullptr) {
                    temp->next = temp->next->next;
                }
                break;
            }
            temp = temp->next;
            i++;
        }

        return head;
    }
};
