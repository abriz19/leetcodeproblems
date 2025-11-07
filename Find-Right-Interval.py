from bisect import bisect_left

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        ans = [-1] * n
        start_vals = [s for s, _ in starts]
        
        for i, (s, e) in enumerate(intervals):
            idx = bisect_left(start_vals, e)  
            if idx < n:
                ans[i] = starts[idx][1]
        
        return ans
