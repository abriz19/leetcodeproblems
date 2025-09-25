from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)  
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  
        
        for i in range(1, n + 1):
            for w in wordSet:
                if i >= len(w) and dp[i - len(w)] and s[i - len(w):i] == w:
                    dp[i] = True
                    break  
        
        return dp[n]
