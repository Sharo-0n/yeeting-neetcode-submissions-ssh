class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        # visited = set() # (r,c)

        def dfs(r, c, visited):
            # false - have not reached and not valid
            if(
                r not in range(ROWS)
                or c not in range(COLS)
                or (r,c) in visited
                or grid[r][c] == 1
            ):
                return 0
            # true - reached the otherside
            elif r == ROWS - 1 and c == COLS - 1:
                return 1
            
            else:
                visited.add((r,c))
                moves = [[1,0], [-1,0], [0,1], [0,-1]]
                count = 0
                for m in moves:
                    count += dfs(r + m[0], c + m[1], visited)
                visited.remove((r,c))
                return count

        return dfs(0,0,set())
        # return self.count