from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(list)
        
        for w in words:
            waiting[w[0]].append(iter(w[1:]))
        
        count = 0
        for c in s:
            advance = waiting[c]
            waiting[c] = []
            for it in advance:
                nxt = next(it, None)
                if nxt:
                    waiting[nxt].append(it)
                else:
                    count += 1  
        return count
