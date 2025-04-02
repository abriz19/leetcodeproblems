class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort()
        ans = 0
        i = len(tasks) - 1
        for t in processorTime:
            ans = max(ans, tasks[i] + t)
            i-=4
        return ans

