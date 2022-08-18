"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        nodeToCopy = {None:None}
        
        def DFS(node):
            if node in nodeToCopy: return nodeToCopy[node]
            
            nodeCopy = Node(node.val)
            nodeToCopy[node] = nodeCopy
            
            for neighbor in node.neighbors:
                nodeCopy.neighbors.append(DFS(neighbor))
            
            return nodeCopy
        
        res = DFS(node)
        return res
