class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots = set(dictionary)
        words = sentence.split()
        
        def replace(word):
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                if prefix in roots:
                    return prefix
            return word
        
        return " ".join(replace(w) for w in words)
