# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head
        curr = head
        while n > 1:
            dummy = dummy.next
            n -= 1

        while dummy.next and dummy.next.next:
            curr = curr.next
            dummy = dummy.next
        
        if curr.next:
            curr.next = curr.next.next
        else:
            return None
        
        return head
        