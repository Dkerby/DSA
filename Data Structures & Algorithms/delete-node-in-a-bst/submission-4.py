# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root != None:
            if root.val < key:
                root.right = self.deleteNode(root.right, key)
            elif root.val > key:
                root.left = self.deleteNode(root.left, key)
            else:
                left = root.left
                right = root.right
                if right == None:
                    root = left
                elif root != None and left != None:
                   currentMin = self.findMin(root.right)
                   root.val = currentMin
                   root.right = self.deleteNode(root.right, root.val) 
                else:
                    root = right

        return root

    def findMin(self, root) -> int:
       if root.left == None:
            return root.val 

       return self.findMin(root.left)