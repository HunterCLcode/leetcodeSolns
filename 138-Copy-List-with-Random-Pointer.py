"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        prev = dummy = Node(0)
        cur, hmap = head, {dummy:Node(0)}
        while cur:
            hmap[cur] = Node(cur.val)
            hmap[prev].next = hmap[cur]
            prev = cur
            cur = cur.next
            
        cur = head
        while cur:
            if cur.random:
                hmap[cur].random = hmap[cur.random]
            cur = cur.next
        return hmap[head] if head else None
