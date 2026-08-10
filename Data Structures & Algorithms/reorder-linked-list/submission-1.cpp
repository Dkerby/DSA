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
    void reorderList(ListNode* head) {
        ListNode* l1 = head;
        ListNode* l2 = head->next;
        ListNode* prev = nullptr;
        ListNode* current = head;
        ListNode* slow = head;
        ListNode* fast = head->next;

        // find the middle node in the list
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        l2 = slow->next;
        slow->next = nullptr;

        // reverse the 2nd list
        current = l2;
        while (current) {
            ListNode* temp = current->next;
            current->next = prev;
            prev = current;
            current = temp;
        }

        while (l1 && prev) {
            ListNode * temp1 = l1->next;
            ListNode * temp2 = prev->next;
            l1->next = prev;
            prev->next = temp1;
            l1 = temp1;
            prev = temp2;
        }
    }
};
