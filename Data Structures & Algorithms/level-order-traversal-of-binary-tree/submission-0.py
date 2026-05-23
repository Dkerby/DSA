# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        arr = []

        if root:
            queue.append(root)

        while len(queue) > 0:
            sublist = []
            for i in range(len(queue)):
                root = queue.popleft()
                sublist.append(root.val)
                if root.left:
                    queue.append(root.left)

                if root.right:
                    queue.append(root.right)
            arr.append(sublist)

        return arr
