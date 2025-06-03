class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash1 = {}
        hash2 = {}
        for i in range(len(s)):
            if s[i] not in hash1:
                hash1[s[i]] = i
            if t[i] not in hash2:
                hash2[t[i]] = i
            if hash1[s[i]] != hash2[t[i]]:
                return False
        return True




        