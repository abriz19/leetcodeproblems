class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2 
        l, r = [0, len(nums) - 1]
        s = []
        while(r >= l):
            if(nums[r] > nums[l]):
                s.append(nums[r])
                r-=1
            else:
                s.append(nums[l])
                l+=1
        s.reverse()
        return s