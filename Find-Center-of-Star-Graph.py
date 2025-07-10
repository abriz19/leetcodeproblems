class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        hash = defaultdict(int)  
        for u, v in edges:
            hash[u] = 1 if not hash[u] else hash[u] + 1
            hash[v] = 1 if not hash[v] else hash[v] + 1
        for key, val in hash.items():
            if val == len(edges):
                return key
        
            
        

        