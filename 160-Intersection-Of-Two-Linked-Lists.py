# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        # Floyd's Tortoise and Hare alg.
        # We create a cycle in A by doing tail.next = head
        # Create a fast and slow pointer through B
        # Once they meet in A, we create third pointer for B
        # Third pointer and slow pointer will meet at intersection
        
        last = headA
        
        while last.next:
            last = last.next
        
        last.next = headA
        
        if not headB.next or not headB.next.next:
            last.next = None
            return None
        
        f, s = headB.next.next, headB.next
        
        while f != s:
            if not f.next or not f.next.next:
                last.next = None
                return None
            f, s = f.next.next, s.next
        
        original = headB
        while original != s:
            original, s = original.next, s.next
        
        last.next = None
        return original
