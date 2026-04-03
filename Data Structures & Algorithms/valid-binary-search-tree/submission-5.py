# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root, minimum, maximum):
            if not root:
                return True
            if minimum >= root.val or root.val >= maximum:
                return False
            if root.left and root.left.val >= root.val:
                return False
            if root.right and root.right.val <= root.val:
                return False
            return True and helper(root.left, minimum, root.val) and helper(root.right, root.val, maximum)

        return helper(root, -1001, 1001)