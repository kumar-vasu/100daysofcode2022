# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        prev = None
        sp = head
        fp = head
        
        if not fp.next:
            return None
        
        if not fp.next.next:
            fp.next = None
            return fp
        
        print(fp.val, sp.val, prev)
        while fp.next:
            prev = sp
            sp = sp.next
            fp = fp.next
            if fp.next:
                fp = fp.next
            
            #print(fp.val, sp.val, prev.val)
        prev.next = sp.next
        
        return head