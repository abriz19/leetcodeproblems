class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        n = len(arr)
        substring_sets = []
        for s in arr:
            subs = set()
            for i in range(len(s)):
                for j in range(i + 1, len(s) + 1):
                    subs.add(s[i:j])
            substring_sets.append(subs)
        
        res = []
        
        for i in range(n):
            unique_subs = []
            for sub in substring_sets[i]:
                if all(sub not in substring_sets[j] for j in range(n) if j != i):
                    unique_subs.append(sub)
            
            if not unique_subs:
                res.append("")
            else:
                unique_subs.sort(key=lambda x: (len(x), x))
                res.append(unique_subs[0])
        
        return res
