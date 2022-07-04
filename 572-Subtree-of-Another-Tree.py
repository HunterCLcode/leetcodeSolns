# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # DFS check at each iteration of the loop to check if it is a subroot
            
        def check(root, subRoot):
            
            if not root and not subRoot:
                return True
            return False if not root or not subRoot else root.val == subRoot.val and check(root.left,subRoot.left) and check(root.right,subRoot.right)
            
        return False if not root else check(root, subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        