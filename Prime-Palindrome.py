import math

class Solution:
    def primePalindrome(self, n: int) -> int:
        if 8 <= n <= 11:
            return 11
        
        for length in range(1, 6):  
            start = 10**(length - 1)
            end = 10**length
            for half in range(start, end):
                s = str(half)
                pal = int(s + s[-2::-1])  
                if pal >= n and self.isPrime(pal):
                    return pal
        return -1  
    
    def isPrime(self, m: int) -> bool:
        if m < 2:
            return False
        if m % 2 == 0:
            return m == 2
        limit = int(math.sqrt(m)) + 1
        for i in range(3, limit, 2):
            if m % i == 0:
                return False
        return True
