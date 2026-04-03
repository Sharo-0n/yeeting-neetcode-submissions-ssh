# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case
        if not p and not q:
            return True
        elif (p and not q) or (not p and q):
            return False

        return (p.val == q.val) & self.isSameTree(p.left, q.left) & self.isSameTree(p.right, q.right)