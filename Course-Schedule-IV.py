from collections import defaultdict, deque

class Solution:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
        
        prereq = [set() for _ in range(numCourses)]
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        while queue:
            course = queue.popleft()
            for nxt in graph[course]:
                prereq[nxt].add(course)
                prereq[nxt] |= prereq[course]
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        
        return [u in prereq[v] for u, v in queries]
