class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-item for item in piles]
        heapq.heapify(piles)
        steps = 0
        while steps < k:
            cur = heapq.heappop(piles)
            r = cur + math.floor(-cur/2)
            heapq.heappush(piles, r)
            steps+=1
        return sum(-item for item in piles)