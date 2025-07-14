from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        if len(s) > 12:
            return []

        def backtrack(i, dots, curIP):
            if dots == 4 and i == len(s):
                res.append(curIP[:-1])
                return
            if dots > 4:
                return
            for j in range(i, min(i + 3, len(s))):
                segment = s[i:j + 1]
                if int(segment) <= 255 and (i == j or s[i] != "0"):
                    backtrack(j + 1, dots + 1, curIP + segment + ".")

        backtrack(0, 0, "")
        return res
