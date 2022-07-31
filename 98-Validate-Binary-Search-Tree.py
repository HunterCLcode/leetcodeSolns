# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Array has two values: must be greater than val1 and less than val2
        def DFS (node, arr):
            if not node: return True
            l = node.val > arr[0] if arr[0] != None else True
            r = node.val < arr[1] if arr[1] != None else True
            return l and r and DFS(node.left, [arr[0],node.val]) and DFS(node.right,[node.val,arr[1]])
            
        return DFS(root, [None, None])

            
