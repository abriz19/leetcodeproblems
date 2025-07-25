class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(prev, index):
            if index == len(s):
                return True
            for j in range(index, len(s)):
                val = int(s[index:j+1])
                if(val+1 == prev) and dfs(val, j+1):
                    return True
            return False
            
        for i in range(len(s) - 1):
            val = int(s[:i+1])
            if dfs(val, i+1):
                return True
        return False