# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        num = max(nums)
        num_index = nums.index(num)
        root = TreeNode(num)
        root.left = self.constructMaximumBinaryTree(nums[:num_index])
        root.right = self.constructMaximumBinaryTree(nums[num_index + 1: ])
        return root
        