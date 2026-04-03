# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # left, right, root
        # 1, 2, 3
        # -1, 2, 3 => @Node max(l + r + n, l + n, n + r, n, 0)

        # -5 -> 0
        # 15 -> 15
        # 5 -> 5
        # 20 -> (15 + 5 + 20, 15 + 20, 20 + 5, 15, 0)
            # n + l + r used for max replacement
            # only max single path sent: (l + n, n + r, n, 0)
        # 10 -> 10
        mps = -1 * float('inf')
        def dfs(n):
            nonlocal mps
            if not n:
                return 0
            l, r = 0, 0
            l = dfs(n.left)
            r = dfs(n.right)
            retval = max(l + n.val, n.val + r, n.val)
            mps = max(mps, retval, l + n.val + r)
            return retval

        dfs(root)
        return mps