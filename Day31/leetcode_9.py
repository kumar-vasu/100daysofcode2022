# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head:
            return head
            
        lead = head
        
        for i in range(n-1):
            if not lead :
                return head
            lead = lead.next

        if not lead.next:
            head = head.next
            return head
        
        lead = lead.next
        follow = head

        while lead.next:
            lead = lead.next
            follow = follow.next

        follow.next = follow.next.next

        return head