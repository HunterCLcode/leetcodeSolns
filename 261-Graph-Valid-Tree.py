class Solution:
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        adjMap = defaultdict(list)
        for n1, n2 in edges:
            adjMap[n1].append(n2)
            adjMap[n2].append(n1)
        
        visit = set()
        def DFS(cur, prev):
  
            if cur in visit: return False

            visit.add(cur)
            res = True

            for node in adjMap[cur]:
                if node != prev: 
                    res &= DFS(node, cur)
            return res

        return DFS(0, -1) and len(visit) == n
