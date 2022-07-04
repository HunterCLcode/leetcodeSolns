# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # T = O(n), S = O(n)
        # Using stack
        stack = [root]
        while stack:
            nodecheck = stack.pop()
            if not nodecheck:
                continue
            l = nodecheck.right
            nodecheck.right = nodecheck.left
            nodecheck.left = l
            stack.append(nodecheck.left)
            stack.append(nodecheck.right)
        return root
            
        