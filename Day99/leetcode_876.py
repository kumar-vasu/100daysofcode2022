# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def traversal(self, head, tail, curr):
        if head == None:
            head = curr
            tail = curr
        else:
            tail.next = curr
            tail = tail.next
        return head, tail
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1 -> create odd/even head, odd/even tail pointer
        2 -> traverse through the linked list
        3 -> upon encountering odd/even val, check if corresponding head is null, If it is: update head and tail              otherwise update only tail till you get to the end of section.
        4 -> Join even head after odd tail
        5 -> return odd head
        """
        if head == None or head.next == None:
            return head
        
        odd_head = None
        odd_tail = None
        even_head = None
        even_tail = None
        index = 0
        
        while head != None:
            if index%2 == 0:
                # for odd indices
                odd_head, odd_tail= self.traversal(odd_head, odd_tail, head)
                print(odd_head.val, odd_tail.val)
            else:
                # for even indices
                even_head, even_tail= self.traversal(even_head, even_tail, head)
                #print(even_head.val, even_tail.val)
            head = head.next
            index+=1
        odd_tail.next = even_head
        even_tail.next = None
        return odd_head