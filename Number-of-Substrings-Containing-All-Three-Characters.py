class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = res = 0
        n = len(s)
        count = defaultdict(int)
        for r in range(n):
            count[s[r]]+=1
            while len(count) == 3:
                res += n - r
                count[s[l]]-=1
                if(count[s[l]] == 0): 
                    count.pop(s[l])
                l+=1
        return res


        