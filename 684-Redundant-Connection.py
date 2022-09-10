class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent, rank = [i for i in range(len(edges))], [1 for i in range(len(edges))]
        
        def union(x, y):
            if rank[x] < rank[y]:
                x, y = y, x
            parent[y] = parent[x]
            rank[x] = max(rank[x], rank[y] + 1)
        
        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        
        for n1, n2 in edges:
            group1, group2 = find(n1 - 1), find(n2 - 1)
            if group1 == group2:
                return [n1, n2]
            union(group1, group2)
