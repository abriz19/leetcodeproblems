class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(img), len(img[0])
        res = [[0] * COLS for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                total, cnt = 0, 0
                for i in range(r-1, r+2):
                    for j in range(c-1, c+2):
                        if i < 0 or i == ROWS or j < 0 or j == COLS:
                            continue
                        cnt+=1
                        total+=img[i][j]
                res[r][c] = total // cnt
        return res
            
        