# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import copy
class Solution:
    def reverse(self, head):
        if not head.next:
            return head, head
        new_head, new_tail = self.reverse(head.next)
        new_tail.next = head
        head.next = None
        return new_head, head
        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        new_head, _ = self.reverse(copy.deepcopy(head))
        curr = head
        
        while new_head and head:
            #print(head.val, new_head.val)
            if head.val != new_head.val:
                return False
            head=head.next
            new_head = new_head.next
            
        return True