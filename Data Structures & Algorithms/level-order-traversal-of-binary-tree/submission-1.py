# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        l = [root]
        retVal = []
        while len(l) > 0:
            new_l = []
            for n in l:
                if n.left:
                    new_l.append(n.left)
                if n.right:
                    new_l.append(n.right)
            retVal.append([node.val for node in l])
            l = new_l
        return retVal