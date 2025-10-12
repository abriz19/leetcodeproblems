class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()  
        built = set()
        longest = ""
        
        for word in words:
            if len(word) == 1 or word[:-1] in built:
                built.add(word)
                if len(word) > len(longest) or (len(word) == len(longest) and word < longest):
                    longest = word
                    
        return longest
