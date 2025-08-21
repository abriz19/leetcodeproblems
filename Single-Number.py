class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash = {c: 0  for c in nums}
        print(hash)
        for n in nums:
            hash[n] += 1
        for n in nums:
            if hash[n] == 1:
                return n