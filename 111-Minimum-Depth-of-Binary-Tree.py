# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        queue = deque([root])
        counter = 0
        
        while queue:
            counter += 1
            for i in range(len(queue)):
                node = queue.popleft()
                
                if not node.left and not node.right: return counter
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        
