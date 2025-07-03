class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hash = {}
        res = [0] * len(nums)
        for i, num in enumerate(nums):
            hash[num] = i
        for operation in operations:
            hash[operation[1]] = hash[operation[0]]
            del hash[operation[0]]
            res[hash[operation[1]]] = operation[1]
        for key in hash:
            res[hash[key]] = key
        return (res)
        


        