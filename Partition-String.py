from typing import List

class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen = set()
        result = []
        i = 0
        n = len(s)
        
        while i < n:
            segment = ""
            for j in range(i, n):
                segment += s[j]
                if segment not in seen:
                    result.append(segment)
                    seen.add(segment)
                    i = j + 1  
                    break
            else:
                i += 1
                
        return result
