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
    ListNode* partition(ListNode* head, int x) {

        ListNode* ptr1 = new ListNode(-1);
        ListNode* ptr2 = new ListNode(-1);
        ListNode* temp = head;
        ListNode* temp1 = ptr1;
        ListNode* temp2 = ptr2;

        while(temp != nullptr) {
            if(temp->val < x) {
                temp1->next = temp;
                temp1 = temp1->next;
            } else {
                temp2->next = temp;
                temp2 = temp2->next;
            }
            temp = temp->next;
        }

        if(ptr1->next == nullptr) {
            return ptr2->next;
        }

        temp1->next = ptr2->next;

        // need to explicitly state this, 
        // else we get an AddressSanitizer 
        // error. makes sense though.
        temp2->next = nullptr;       
           
        return ptr1->next;

    }
};