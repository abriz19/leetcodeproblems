from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        visited = [0] * numCourses
        result = []
        self.valid = True

        def dfs(course):
            if not self.valid:
                return
            visited[course] = 1
            for neighbor in graph[course]:
                if visited[neighbor] == 0:
                    dfs(neighbor)
                elif visited[neighbor] == 1:
                    self.valid = False
            visited[course] = 2
            result.append(course)

        for i in range(numCourses):
            if visited[i] == 0:
                dfs(i)

        return result[::-1] if self.valid else []
