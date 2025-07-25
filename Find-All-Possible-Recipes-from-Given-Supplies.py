from collections import defaultdict, deque
from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        can_cook = {s: True for s in supplies}
        recipe_index = {r: i for i, r in enumerate(recipes)}
        def dfs(r):
            if r in can_cook:
                return can_cook[r]
            if r not in recipe_index:
                return False
            can_cook[r] = False
            for nei in ingredients[recipe_index[r]]:
                if not dfs(nei):
                    return False
            can_cook[r] = True
            return True
        return [r for r in recipes if dfs(r)]
            

