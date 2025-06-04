class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        while l <= r:
            m = (l+r) // 2
            if num == m **2:
                return True
            elif num > m**2:
                l = m + 1
            else:
                r = m - 1
        return False 

        
        