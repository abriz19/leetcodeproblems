class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeat = -(-len(b) // len(a))  # same as math.ceil(len(b)/len(a))
        
        for i in range(repeat, repeat + 2):
            if b in a * i:
                return i
        return -1
