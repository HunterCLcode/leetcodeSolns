# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS w/ Stack
        if not root:
            return 0
        stack = [(root,1)]
        best = 1
        while stack:
            holder = stack.pop()
            node = holder[0]
            lvl = holder[1]
            
            if node:
                best = max(lvl,best)
                stack.append((node.left,lvl + 1))
                stack.append((node.right,lvl + 1))
        return best
                
                
            