class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        while head:
            if head in seen:
                return head
            else:
                seen.add(head)
                head = head.next
        return None
                