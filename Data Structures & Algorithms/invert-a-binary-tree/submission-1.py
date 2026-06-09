# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        # save off the original nodes for traversal
        originalLeft = root.left
        originalRight = root.right
    
        # traverse the left
        if originalLeft:
            self.invertTree(originalLeft)

        # peform the swap
        temp = root.left
        root.left = root.right
        root.right = temp

        # traverse the right
        if originalRight:
            self.invertTree(originalRight)
        
        return root

