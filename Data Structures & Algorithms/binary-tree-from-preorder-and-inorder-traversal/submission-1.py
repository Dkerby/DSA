# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None 

        root = TreeNode(preorder[0])

        for i in range(0, len(inorder)):
            if root.val == inorder[i]:
                print(preorder[1: i + 1])
                root.left = self.buildTree(preorder[1: i + 1], inorder[0:i])  
                root.right = self.buildTree(preorder[i + 1: len(preorder)], inorder[i + 1: len(inorder)])
                break

        return root