# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # DFS and return whether the path contains the sum (True) while passing down the node sum
        def DFS(node, num):
            newSum = num + node.val
            if not node.left and not node.right: return newSum == targetSum
            left = DFS(node.left, newSum) if node.left else False 
            right = DFS(node.right, newSum) if node.right else False
            return left or right
        
        return DFS(root, 0) if root else False
