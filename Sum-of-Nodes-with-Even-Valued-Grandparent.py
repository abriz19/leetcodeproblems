# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(root, parent, grandParent):
            if not root:
                return 0
            res = 0
            if (grandParent and grandParent.val % 2 == 0):
                res += root.val
            return res + dfs(root.left, root, parent) + dfs(root.right, root, parent)
        return dfs(root, None, None)
        