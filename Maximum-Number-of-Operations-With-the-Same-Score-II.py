from functools import lru_cache
from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(i, j, target):
            if j - i + 1 < 2:
                return 0
            res = 0
            if i + 1 <= j and nums[i] + nums[i + 1] == target:
                res = max(res, 1 + dfs(i + 2, j, target))
            if j - 1 >= i and nums[j - 1] + nums[j] == target:
                res = max(res, 1 + dfs(i, j - 2, target))
            if nums[i] + nums[j] == target:
                res = max(res, 1 + dfs(i + 1, j - 1, target))
            return res

        ans = 0
        if n >= 2:
            ans = max(
                dfs(0, n - 1, nums[0] + nums[1]),
                dfs(0, n - 1, nums[-2] + nums[-1]),
                dfs(0, n - 1, nums[0] + nums[-1]),
            )
        return ans
