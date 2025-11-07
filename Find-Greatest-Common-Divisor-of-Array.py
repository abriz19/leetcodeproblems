class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)
        if(max_num % min_num == 0):
            return min_num
        for num in range(min_num // 2, 1, -1):
            print(num)
            if(min_num % num == 0 and max_num % num == 0):
                return num
        return 1