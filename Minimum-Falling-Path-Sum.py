class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        for i in range(n-2, -1, -1):
            for j in range(n):
                down = matrix[i+1][j]
                down_left = matrix[i+1][j-1] if j > 0 else float('inf')
                down_right = matrix[i+1][j+1] if j < n-1 else float('inf')
                matrix[i][j] += min(down, down_left, down_right)
        
        return min(matrix[0])

        