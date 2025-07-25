class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        queue = deque()
        queue.append((entrance[0], entrance[1], 0))
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        visited = set()
        visited.add((entrance[0], entrance[1]))

        while queue:
            r, c, steps = queue.popleft()
            
            if (r != entrance[0] or c != entrance[1]) and (r == 0 or r == rows-1 or c == 0 or c == cols-1):
                return steps

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '.' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, steps + 1))

        return -1