# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next and head.next.next:
            pn, cn, nn = head, head.next.next, head.next.next

            for i in range(n - 1):
                if not nn:
                    return head.next
                nn = nn.next

            while nn:
                pn = pn.next
                cn = cn.next
                nn = nn.next
            pn.next = cn
            
        elif head.next:
            if n == 1: head.next = None
            else: head = head.next
        else: head = None
        return head
