# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def inorder_dfs(node):
            if not node:
                return
            inorder_dfs(node.left)
            arr.append(node.val)
            inorder_dfs(node.right)
        inorder_dfs(root)
        return arr[k-1]