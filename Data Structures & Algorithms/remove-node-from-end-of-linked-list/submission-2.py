# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = head

        while n > 0:
            curr = curr.next
            n -= 1

        while curr and curr.next:
            curr = curr.next
            head = head.next
        
        if not curr:
            return head.next
            
        head.next = head.next.next
        
        return dummy.next
        