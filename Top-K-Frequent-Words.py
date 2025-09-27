class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        sorted_words = sorted(count.keys(), key=lambda w: (-count[w], w))
        return sorted_words[:k]
