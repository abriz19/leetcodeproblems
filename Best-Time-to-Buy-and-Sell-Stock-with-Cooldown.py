class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        hold, sold, rest = -prices[0], float('-inf'), 0

        for price in prices[1:]:
            prev_hold, prev_sold, prev_rest = hold, sold, rest
            hold = max(prev_hold, prev_rest - price)
            sold = prev_hold + price
            rest = max(prev_rest, prev_sold)

        return max(sold, rest)
