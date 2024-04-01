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
    int getDecimalValue(ListNode* head) {
        int n = 0;
        int num = 0;
        
        ListNode* temp = head;

        while(temp) {
            n++;
            temp = temp->next;
        }

        temp = head;

        while(temp) {
            num += (pow(2, n - 1) * temp->val);
            n--;
            temp = temp->next;
        }

        return num;

    }
};