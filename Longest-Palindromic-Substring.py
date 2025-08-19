class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
          return ""

        start, end = 0, 0

        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1  

        for i in range(len(s)):
            l1, r1 = expandAroundCenter(i, i)
            l2, r2 = expandAroundCenter(i, i + 1)

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]

        