from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        res = []
        len_p = len(p)
        count_p = Counter(p)
        count_s = Counter()
        
        for i, char in enumerate(s):
            count_s[char] += 1
            
            # Keep window size = len_p
            if i >= len_p:
                left_char = s[i - len_p]
                if count_s[left_char] == 1:
                    del count_s[left_char]
                else:
                    count_s[left_char] -= 1
            
            # Check if current window matches p
            if count_s == count_p:
                res.append(i - len_p + 1)
        
        return res
