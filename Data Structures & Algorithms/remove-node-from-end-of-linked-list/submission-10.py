# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None 

        dummy = ListNode(0)
        dummy.next = head 
        slow = dummy 
        fast = head

        # fast will be at the last node in the list
        # slow will be at the head still
        for i in range(n):
            fast = fast.next

        # move both of them together simultaneously
        # fast will be at the end, and slow will be right
        # where we need to remove the node
        while fast:
            fast = fast.next
            slow = slow.next

        # skip over the node, removing it
        slow.next = slow.next.next

        return dummy.next
