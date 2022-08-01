# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def goodNodesRecur(node, val):
            if not node: return 0
            val = max(val, node.val)
            res = 1 if node.val == val else 0
            return res + goodNodesRecur(node.left, val) + goodNodesRecur(node.right,val)
        
        return goodNodesRecur(root, -10000)
