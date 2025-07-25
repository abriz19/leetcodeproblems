class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = defaultdict(int)
        res = []
        for num in nums:
            hash[num] = 1 if not hash[num] else hash[num]+1
        data = sorted(hash.items(), reverse=True, key= lambda item: item[1])
        print(data)
        for i in range(k):
            res.append(data[i][0])
        return res
        

        