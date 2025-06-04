class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        while left<=right:
            mid = (left + right) //2
            if letters[mid] > target:
                right = mid - 1
            if letters[mid] <= target:
                left = mid + 1
        if left == len(letters):
            return letters[0]
        else: 
            return letters[left]
        
            


            

        