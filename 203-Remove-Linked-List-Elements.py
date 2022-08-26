# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        p, c = dummy, head
        
        while c:
            if c.val == val:
                p.next = c.next
                c = p
            p = c
            c = c.next
        
        return dummy.next
            
        
