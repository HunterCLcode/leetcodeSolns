class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def DFS(path, parenLeft, parenClose):
            if not parenLeft and not parenClose: res.append(path)

            if parenLeft: DFS(path + '(', parenLeft - 1, parenClose + 1)
            if parenClose: DFS(path + ')', parenLeft, parenClose - 1)

        DFS("", n, 0)
        return res
