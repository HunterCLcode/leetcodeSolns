# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        dummy = TreeNode(0, None, root)
        n, stack = -1, [dummy]
        
        while stack:
            node = stack.pop()
            n += 1
            if n == k: return node.val
            
            if node.right:
                node = node.right
                stack.append(node)
                while node.left:
                    stack.append(node.left)
                    node = node.left
