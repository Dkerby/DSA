# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None or subRoot == None:
            return root == subRoot

        print("isSubtree", root.val, subRoot.val)
        # traverse the root tree, and if the value of the subroot matches test it
        if root.val == subRoot.val:
            if self.isIdentical(root, subRoot):
                return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isIdentical(self, a, b):
        if a == None or b == None:
            return a == b

        print("isIdentical", a.val, b.val)
        if not a.val == b.val:
            return False
        
        if not (self.isIdentical(a.left, b.left) and self.isIdentical(a.right, b.right)):
           return False

        print("returned True")
        return True 