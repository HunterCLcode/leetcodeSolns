class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {i : [] for i in range(numCourses)}
        for course, pre in prerequisites:
            courses[course].append(pre)
        
        path = set()
        def DFS(i):
            if not courses[i]: return True
            if i in path: return False
            
            path.add(i)
            for course in courses[i]:
                if not DFS(course): return False
            courses[i] = []
            return True

        for course in courses:
            if not DFS(course): return False
        return True
