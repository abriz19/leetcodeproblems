class Solution:
    def findComplement(self, num: int) -> int:
        res = ""
        n = num 
        while (n > 0): 
            res+=str(n%2)
            n = n // 2
        ans = 0
        res = res[::-1]
        print(res)
        for i in range(len(res) - 1, -1, -1):
            if res[i] == "0":
                power = len(res) - i - 1
                ans += math.pow(2, power)
        return int(ans)