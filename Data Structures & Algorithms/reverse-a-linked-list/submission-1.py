# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if head == None or head.next == None:
                return head
            else:
                # get the reverse sublist, withthout head attached
                reversedListHead = self.reverseList(head.next)
                # the current tail is head.next
                # make a variable for the tail
                tail = head.next
                # point tail to the former head node as the next in line
                tail.next = head 
                # clear head's next pointer, since it is now the new tail 
                head.next = None
                return reversedListHead

