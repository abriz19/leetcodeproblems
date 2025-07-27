class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        ops = 0
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                pieces = (nums[i] + nums[i + 1] - 1) // nums[i + 1]
                ops += pieces - 1
                nums[i] = nums[i] // pieces
        return ops
