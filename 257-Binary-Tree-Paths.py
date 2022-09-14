class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(node, path):
            if not node.left and not node.right:
                res.append(path[:])
                return
            if node.left: dfs(node.left, path + "->" + str(node.left.val))
            if node.right: dfs(node.right, path + "->" + str(node.right.val))
        
        dfs(root, str(root.val))
        return res
            
