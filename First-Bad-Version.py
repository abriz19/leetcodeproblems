# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        isBad = isBadVersion(n)
        l, r = 1, n
        while l < r:
            m = (l + r) // 2
            isBad = isBadVersion(m)
            if(isBad):
                r = m
            else:
                l = m + 1
        return l