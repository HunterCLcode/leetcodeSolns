class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dummy = latest = TreeNode(0)
        stack = []
        p, i = 0, 0
        
        while p < len(preorder):
            node = TreeNode(preorder[p])
            latest.right = node
            stack.append(node)
            p += 1
            while inorder[i] != stack[-1].val:
                node = TreeNode(preorder[p])
                stack[-1].left = node
                stack.append(node)
                p += 1
            while stack and inorder[i] == stack[-1].val:
                latest = stack.pop()
                i += 1
        return dummy.right
        
