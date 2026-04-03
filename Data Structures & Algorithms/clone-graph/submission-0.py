"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # node[i] = [node i's adj nodes]
        visited = {} # og node: new node
        def dfs(og):
            if not og:
                return None
            if og in visited:
                return visited[og]
            new = Node()
            new.val = og.val
            new_adj = []
            visited[og] = new
            for n in og.neighbors:
                new_adj_node = dfs(n)
                new_adj.append(new_adj_node)
            new.neighbors = new_adj
            return new
        return dfs(node)

