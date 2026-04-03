# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # bfs to search for subRoot
        stack= [root]
        while len(stack) > 0:
            curr = stack.pop()
            # check if beginning node is the same
            if curr.val == subRoot.val:
                print("same")
                # check if same tree
                if self.isSameTree(curr, subRoot):
                    return True
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif (not p and q) or (p and not q):
            return False

        return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)