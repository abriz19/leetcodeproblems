import collections
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = collections.defaultdict(int)
        l, res, total = 0, 0, 0
        for r in range(len(fruits)):
            count[fruits[r]]+=1
            total+=1
            while len(count) > 2:
                total-=1
                count[fruits[l]]-=1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l+=1
            res = max(res, total)
        return res

        