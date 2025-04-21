class Solution:
    def smallestNumber(self, num: int) -> int:
       if(num == 0):
            return num
       num = list(str(num))
       if ("-" in num):
            num.sort(reverse = True)
            num.remove("-")
            num.insert(0, "-")
       else:
            num.sort()
            cnt = num.count("0")
            if(cnt>0):
                num[0] = num[cnt]
                num[1:cnt+1] = ["0"] * cnt
       num = "".join(num)
       return int(num)

    
            
        