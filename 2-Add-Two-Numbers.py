# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2, carry = l1, l2, 0
        res = cur = ListNode()
        
        while p1 or p2:
            n1, n2 = 0, 0
            if p1:
                n1 = p1.val
                p1 = p1.next
            if p2:
                n2 = p2.val
                p2 = p2.next
            sumN = n1 + n2 + carry
            cur.next = ListNode(sumN % 10)
            cur = cur.next
            carry = sumN // 10
        
        if carry: cur.next = ListNode(carry)
        return res.next
                
        
