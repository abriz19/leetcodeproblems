# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, curSum, curArr):
            if not node:
                return []
            curSum+=node.val
            curArr.append(node.val)
            if not node.left and not node.right and curSum == targetSum:
                res.append(curArr.copy())
            dfs(node.left, curSum, curArr)
            dfs(node.right, curSum, curArr)
            curArr.pop()
        dfs(root, 0, [])
        return res

        