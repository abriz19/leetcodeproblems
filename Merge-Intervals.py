class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval: interval[0])
        output = [intervals[0]]
        for start, end in intervals:
            lastInterval = output[-1]
            if start <= lastInterval[1]:
                lastInterval[1] = max(lastInterval[1], end)
            else:
                output.append([start, end])
        return output
        