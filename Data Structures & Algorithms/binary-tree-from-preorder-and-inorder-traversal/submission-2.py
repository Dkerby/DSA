# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # build a hashmap of of the node value to the index in the inorder array
        indices = {}
        for i in range(len(inorder)):
            indices[inorder[i]] = i

        # instantiate a global variable since pass by reference doesn't work in python
        self.preorderIndex = 0

        def dfs(leftIndex, rightIndex):
            # if we've hit the base case, return
            if leftIndex > rightIndex:
                return None 

            # retrieve the root value using the index
            rootVal = preorder[self.preorderIndex]
            # increment the global preorder index counter
            self.preorderIndex += 1
            # instantiate the local root node
            root = TreeNode(rootVal)
            # get the mid index from the inorder traversal hashmap we built earlier
            midIndex = indices[rootVal]
            # use the mid index to get the left subtree
            root.left = dfs(leftIndex, midIndex - 1)
            # use the mid index to get the right subtree
            root.right = dfs(midIndex + 1, rightIndex)
            return root

        # kick off the dfs function using the left and right index of the inorder array
        return dfs(0, len(inorder) - 1)