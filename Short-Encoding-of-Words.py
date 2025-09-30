from typing import List

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        # remove duplicates
        word_set = set(words)

        # remove suffixes
        for word in words:
            for i in range(1, len(word)):
                word_set.discard(word[i:])

        # length of encoding = sum of (len(word) + 1 for '#')
        return sum(len(word) + 1 for word in word_set)
