class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        val = sorted(nums, reverse=True)
        print(val)
        return val[k-1]