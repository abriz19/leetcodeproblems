class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()

        def dfs(r, c):
            if (
                r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or grid[r][c] == 0
                or (r, c) in seen
            ):
                return 0
            seen.add((r, c))
            return 1 + dfs(r, c+1) + dfs(r, c-1) + dfs(r-1, c) + dfs(r+1, c)
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r,c))
        return area
