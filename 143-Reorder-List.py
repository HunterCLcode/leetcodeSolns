# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next or not head.next.next: return head
        
        mid = cur = head
        while cur and cur.next:
            mid = mid.next
            cur = cur.next.next
        
        prev, cur = mid, mid.next
        prev.next = None
        while cur:
            n = cur.next
            cur.next = prev
            prev = cur
            cur = n
        
        l, r = head, prev
        
        while l.next and r.next:
            t = l.next
            l.next = r
            l = t
            
            t = r.next
            r.next = l
            r = t
        
