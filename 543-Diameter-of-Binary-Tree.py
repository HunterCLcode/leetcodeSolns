# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Iteratively find the lowest, and second lowest node
        return 0 if not root else self.recursiveBinaryTree(root)[1]
        
    def recursiveBinaryTree(self, node):
        # Return height & diameter
        lh, ld, rh, rd = 0,0,0,0
        if node.left:
            lh, ld = self.recursiveBinaryTree(node.left)
        if node.right:
            rh, rd = self.recursiveBinaryTree(node.right)
        return [max(lh,rh) + 1, max(lh + rh, ld, rd)]
        
        
        