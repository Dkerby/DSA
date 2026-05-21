# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        leftCount = 0 if root == None else self.dfs(root.left, 0)
        rightCount = 0 if root == None else self.dfs(root.right, 0)

        if leftCount < 0 or rightCount < 0:
            return False
        else:
            diff = leftCount - rightCount

        return diff > -2 and diff < 2 

    def dfs(self, root, depth) -> int:
        if root == None:
            return depth 
        
        leftCount = self.dfs(root.left, depth)
        rightCount = self.dfs(root.right, depth)

        diff = leftCount - rightCount

        if not(diff > -2 and diff < 2):
            depth = -2
        else:
            depth = 1 + max(self.dfs(root.left, depth), self.dfs(root.right, depth))

        return depth
        