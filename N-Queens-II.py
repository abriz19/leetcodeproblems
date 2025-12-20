1class Solution:
2    def totalNQueens(self, n: int) -> int:
3        col = set()
4        posDiag = set()
5        negDiag = set() 
6        board = [['.'] * n for _ in range(n)]
7        res = 0
8        def backtrack(r):
9            nonlocal res
10            if r == n:
11                res = res + 1
12                return
13            for c in range(n):
14                if c in col or r+c in posDiag or r-c in negDiag:
15                    continue
16                col.add(c)
17                posDiag.add(r+c)  
18                negDiag.add(r-c)
19                board[r][c] = 'Q'  
20
21                backtrack(r+1)
22
23                col.remove(c)
24                posDiag.remove(r+c)  
25                negDiag.remove(r-c)
26                board[r][c] = '.'  
27        backtrack(0)
28        return res
29