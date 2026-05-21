# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        array = []
        self.inOrderTraversal(root, array)

        return array[k - 1]

    def inOrderTraversal(self, root: Optional[TreeNode], array: List):
        if root != None:
            self.inOrderTraversal(root.left, array)
            array.append(root.val)
            # print(array)
            self.inOrderTraversal(root.right, array)


