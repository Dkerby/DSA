# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # return False if we hit the base case
        if root == None:
            return False

        targetSum -= root.val 

        # if the node is leaf node, check if it has the right value
        if not root.left and not root.right and targetSum == 0:
            return True

        # if it's not a leaf node, keep looking at both left and right paths
        if self.hasPathSum(root.left, targetSum):
            return True

        if self.hasPathSum(root.right, targetSum):
            return True

        # we don't have valid path, so we need to backtrack
        return False