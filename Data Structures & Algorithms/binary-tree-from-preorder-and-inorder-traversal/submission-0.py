# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder = [1,2,3,4], inorder = [2,1,3,4]
        # preorder[0] -> parent node
        # io = io left of preorder[0] is left of parent node
        # io = io right of preorder[0] is right of parent node

        # def helper(po, io):
        if not preorder or not inorder:
            return None
        
        val = preorder[0]
        mid = inorder.index(val)
        currNode = TreeNode(val)
        currNode.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        currNode.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return currNode