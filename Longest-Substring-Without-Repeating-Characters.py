class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        o = l = r = 0
        sub = {}
        while(r<len(s)):
            if not sub.get(s[r], False):
                sub[s[r]] = r
                r+=1
            else:
                l = r = sub[s[r]] + 1
                sub = {}
            o = max(o, len(sub))
        return o if o != 0 else len(sub)

            
        