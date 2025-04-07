class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        stack = []
        for x in range(len(nums)):
            stack.append(sum(nums[:x+1]))
        return stack

        