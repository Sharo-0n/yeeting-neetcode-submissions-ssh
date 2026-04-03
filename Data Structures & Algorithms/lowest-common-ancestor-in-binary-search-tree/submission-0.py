# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ## base cases
        # DNE
        if not root:
            return None

        # root is one of the two
        if root.val == p.val or root.val == q.val:
            return root
        
        # Where do the results diverge (root) is in between the two
        if (root.val > p.val and root.val < q.val) or (root.val > q.val and root.val < p.val):
            return root

        ## loop!
        return self.lowestCommonAncestor(root.left, p, q) if self.lowestCommonAncestor(root.left, p, q) else self.lowestCommonAncestor(root.right, p, q)