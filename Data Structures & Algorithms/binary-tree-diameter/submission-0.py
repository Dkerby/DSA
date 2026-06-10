# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = [0]
        self.dfs(root, maxDiameter)

        return maxDiameter[0]

    def dfs(self, root, maxDiameter) -> int:
        # don't add to the height if the node is null
        if not root:
            return 0

        # get the max diameter for both the left and right subtrees
        left = self.dfs(root.left, maxDiameter)
        right = self.dfs(root.right, maxDiameter)

        # get the current diameter for a path passing through the current node
        currentDiameter = left + right

        # if the path through the current node is the largest we've seen so far, save it
        if currentDiameter > maxDiameter[0]:
            maxDiameter[0] = currentDiameter

        # while traversing through the tree, we find the max of the left and right heights
        # and add 1 for the current node we're on
        return max(left, right) + 1
