# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node: return [True, 0]
            l, r = dfs(node.left), dfs(node.right)
            return [l[0] and r[0] and (abs(l[1] - r[1]) < 2), max(l[1],r[1]) + 1]
        return dfs(root)[0]
            
        