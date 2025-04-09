class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r, res = 0, len(people)-1, 0
        while(l<=r):
            remain = limit - people[r]
            res+=1
            r-=1
            if remain >= people[l] and l<=r:
                l+=1
        return res