# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None 

        current = head
        total = 0

        # find the last node in the list
        while current:
            total += 1
            current = current.next

        # current is going to be equal to the last node in the list
        # and we now have a count of how many nodes are in the list
        prev = None
        current = head
        nth = total - n
        if nth == 0:
            return head.next

        while current and nth > 0:
            nth -= 1
            prev = current
            current = current.next
        
        # now we're halted with the previous node and the next node in hand,
        # we can remove the nth node
        if not current:
            prev.next = None
        else:
            prev.next = current.next

        return head
