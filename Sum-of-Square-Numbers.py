class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        arr = []
        for i in range(int(sqrt(c)) + 1):
            arr.append(i**2)
        l, r = 0, len(arr) - 1
        while(l<=r):
            if(arr[l] + arr[r] == c):
                return True
            elif(arr[l] + arr[r] > c):
                r-=1
            else:
                l+=1
        return False

