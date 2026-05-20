# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        items = [] 

        self.dfs(root, items)

        return items

    def dfs(self, root: Optional[TreeNode], items: List[int]):
        if root == None:
            return []

        self.dfs(root.left, items)
        items.append(root.val)
        self.dfs(root.right, items)
        