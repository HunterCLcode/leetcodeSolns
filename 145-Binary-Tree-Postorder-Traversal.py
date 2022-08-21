# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        
        def DFS(node):
            if not node: return
            DFS(node.left)
            DFS(node.right)
            res.append(node.val)
            return
            
            
        DFS(root)    
        
        return res
