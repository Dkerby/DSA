# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        val = [0]
        self.inOrderTraversal(root, val, [k])

        return val[0]

    def inOrderTraversal(self, root: Optional[TreeNode], val:list, k: List):
        if root == None or k[0] < 0:
            return

        self.inOrderTraversal(root.left, val, k)
        k[0] -= 1

        if k[0] == 0:
            val[0] = root.val

        self.inOrderTraversal(root.right, val, k)

        