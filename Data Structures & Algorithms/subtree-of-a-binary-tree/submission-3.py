# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isEquivalent(root, subRoot):
            return True        
        return False or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isEquivalent(self, p, q) -> bool:
        if not p and not q:
            return True
        if not p:
            return False
        if not q:
            return False
        return p.val == q.val and self.isEquivalent(p.left, q.left) and self.isEquivalent(p.right, q.right)