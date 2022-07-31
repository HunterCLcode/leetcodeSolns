# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def goodNodesRecur(node, arr):
            if not node: return 0
            arr.append(node.val)
            res = 1 if node.val == max(arr) else 0
            res += goodNodesRecur(node.left,arr[:]) + goodNodesRecur(node.right,arr[:])
            return res
        
        return goodNodesRecur(root, [])
