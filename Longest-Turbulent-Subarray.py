class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0, 1
        res, prev = 1, ""
        while(r < len(arr)):
            if arr[r - 1] > arr[r] and prev != ">":
                prev = ">"
                res = max(res, r-l+1)
                r+=1
            elif arr[r-1] < arr[r] and prev != "<":
                prev = "<"
                res = max(res, r-l+1)
                r+=1
            else:
                prev = ""
                r = r if arr[r] != arr[r-1] else r+1
                l = r - 1
        return res















            