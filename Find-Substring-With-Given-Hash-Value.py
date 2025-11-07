class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        h = 0
        power_k = pow(power, k, modulo)  
        res_index = n  
        
        def val(ch):
            return ord(ch) - ord('a') + 1
        
        for i in range(n - 1, -1, -1):
            h = (h * power + val(s[i])) % modulo
            
            if i + k < n:
                h = (h - val(s[i + k]) * power_k) % modulo  
            
            if i + k <= n and h == hashValue:
                res_index = i  
        
        return s[res_index:res_index + k]
