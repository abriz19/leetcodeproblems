class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hash1 = {}
        res = 0
        for c in chars:
            hash1[c] = hash1[c] + 1 if c in hash1 else 1
        for word in words:
            can_formed = True
            copy = hash1.copy()
            for w in word:
                if w not in copy or copy[w] <= 0:
                    can_formed = False
                    break
                else:
                    copy[w] -= 1
            if not can_formed:
                continue
            res += len(word)
        return res
            

                



        