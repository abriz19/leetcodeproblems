class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)  
        
        for i in range(n - 1, -1, -1):  
            points, brainpower = questions[i]
            skip = dp[i + 1]
            solve = points
            if i + brainpower + 1 < n:
                solve += dp[i + brainpower + 1]
            dp[i] = max(skip, solve)
        
        return dp[0]
