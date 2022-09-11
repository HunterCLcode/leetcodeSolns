class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visit, frontier = set(), [[0, tuple(points[0])]]
        output = 0
        
        while len(visit) != len(points):
            dist, point = heapq.heappop(frontier)
            if point in visit: continue
            visit.add(point)
            output += dist
            
            for target in points:
                if tuple(target) in visit: continue
                heapq.heappush(frontier, [abs(target[0] - point[0]) + abs(target[1] - point[1]), tuple(target)])
        return output        
