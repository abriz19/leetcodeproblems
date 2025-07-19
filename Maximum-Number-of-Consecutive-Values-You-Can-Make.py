class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        target = 1
        for coin in coins:
            if coin > target:
                break
            target += coin
        return target
