class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder =Counter( {0: 1})
        ans = 0
        sum = 0
        for num in nums:
            sum = (sum + num) % k
            ans+=remainder[sum]
            remainder[sum]+=1
        return ans

        