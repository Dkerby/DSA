# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while cur1 or cur2 or carry:
            val = (cur1.val if cur1 else 0) + (cur2.val if cur2 else 0) + carry
            carry = val // 10

            current.next = ListNode(val % 10) 
            current = current.next
            cur1 = cur1.next if cur1 else None 
            cur2 = cur2.next if cur2 else None

        return dummy.next
            