class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        for currentDay in range(n):
            while stack and temperatures[currentDay] > temperatures[stack[-1]]:
                previousDay = stack.pop()
                result[previousDay] = currentDay - previousDay
                
            stack.append(currentDay)
            
        return result  

        