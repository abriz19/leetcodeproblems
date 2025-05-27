from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        res = []

        for num in count1:
            if num in count2:
                times = min(count1[num], count2[num])
                res.extend([num] * times)

        return res

 
        
        