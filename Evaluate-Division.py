from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val
        
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            visited.add(start)
            for neighbor, val in graph[start].items():
                if neighbor in visited:
                    continue
                res = dfs(neighbor, end, visited)
                if res != -1.0:
                    return res * val
            return -1.0
        
        results = []
        for a, b in queries:
            results.append(dfs(a, b, set()))
        
        return results
