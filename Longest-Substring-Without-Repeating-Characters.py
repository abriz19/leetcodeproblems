class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        sub = {}
        max_length = 0

        for r in range(len(s)):
            if s[r] in sub and sub[s[r]] >= l:
                l = sub[s[r]] + 1 
            sub[s[r]] = r 
            max_length = max(max_length, r - l + 1)

        return max_length