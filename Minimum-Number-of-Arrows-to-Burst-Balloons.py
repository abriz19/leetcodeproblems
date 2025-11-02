class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Step 1: Sort by end coordinate
        points.sort(key=lambda x: x[1])

        arrows = 1
        end = points[0][1]

        # Step 2: Traverse the balloons
        for start, finish in points[1:]:
            if start > end:
                arrows += 1
                end = finish  # Move to new balloon's end
        
        return arrows
