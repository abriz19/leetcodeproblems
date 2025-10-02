from functools import lru_cache
from typing import List

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        word_set = set(dictionary)  # faster lookup
        n = len(s)

        @lru_cache(None)
        def dp(i: int) -> int:
            if i == n:
                return 0

            # Option 1: skip this character
            res = 1 + dp(i + 1)

            # Option 2: try matching words
            for word in word_set:
                if s.startswith(word, i):
                    res = min(res, dp(i + len(word)))
            
            return res

        return dp(0)
