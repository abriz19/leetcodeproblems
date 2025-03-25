class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i, n = 0, len(arr) - 1

        while(i < n):
            if(arr[i] == 0):
                arr.insert(i+1, 0)
                del arr[len(arr) - 1]
                i+=2
            else:
                i+=1



        
        