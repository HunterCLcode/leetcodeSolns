class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minheap, output = [], 0
        visit = set([k])
        adjList = {i:[] for i in range(1, n + 1)}
        
        # Create adj list where node -> list of [target node, time]
        for source, target, time in times:
            adjList[source].append([target,time])
        
        # Append all first travel times from node k
        for target, time in adjList[k]:
            heapq.heappush(minheap, [time, target])
        
        while minheap and len(visit) != n:
            output, node = heapq.heappop(minheap)
            if node in visit: continue
            visit.add(node)

            for target, time in adjList[node]:
                if target not in visit:
                    heapq.heappush(minheap, [output + time, target])
        
        return output if len(visit) == n else -1
