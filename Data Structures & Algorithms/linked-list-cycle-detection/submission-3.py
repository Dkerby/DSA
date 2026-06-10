# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        # use Floyd's Cycle-Finding algoritm
        # AKA tortoise and hare
        slow = head 
        fast = head.next 

        # keep looping until the leading pointer hits a None
        while fast and fast.next:
            # check for a cycle
            if slow == fast:
                return True

            # advance the pointers
            # slow + 1, fast + 2
            slow = slow.next
            fast = fast.next.next

        return False 