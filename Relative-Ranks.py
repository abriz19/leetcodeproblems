class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse = True)
        for i in range(len(score)):
            if sorted_score.index(score[i]) == 0:
                score[i] = "Gold Medal"
            elif sorted_score.index(score[i]) == 1:
                score[i] = "Silver Medal"
            elif sorted_score.index(score[i]) == 2:
                score[i] = "Bronze Medal"
            else:
                score[i] = str(sorted_score.index(score[i]) + 1)
        return score
