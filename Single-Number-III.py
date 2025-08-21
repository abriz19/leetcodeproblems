class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hash = {c: 0  for c in nums}
        ans = []
        for n in nums:
            hash[n] += 1
        for n in nums:
            if hash[n] == 1:
                ans.append(n)
        return ans