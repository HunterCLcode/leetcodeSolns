class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseMap = {i : [] for i in range(numCourses)}
        for course, pre in prerequisites:
            courseMap[course].append(pre)
        
        path, res = set(), []
        
        def DFS(i):
            if not courseMap[i]:
                if i not in path:
                    path.add(i)
                    res.append(i)
                return True
            if i in path: return False
            
            path.add(i)
            for course in courseMap[i]:
                if not DFS(course): return False
            res.append(i)
            courseMap[i] = []
            return True
        
        for course in courseMap:
            if not DFS(course): return []
        return res
