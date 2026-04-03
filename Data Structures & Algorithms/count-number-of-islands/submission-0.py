class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) < 0 or len(grid[0]) < 0:
            return
        ROW = len(grid)
        COL = len(grid[0])
        visited = set() # (r,c)

        def visitIslandDFS(r, c):
            if r >= 0 and r < ROW and c >= 0 and c < COL and (r,c) not in visited and grid[r][c] == "1":
                visited.add((r, c)) 
                for coor in [(0,-1), (-1, 0), (0, 1), (1, 0)]:
                    visitIslandDFS(r + coor[0], c + coor[1])

        numIslands = 0
        for r in range(ROW):
            for c in range(COL):
                if (r,c) not in visited and grid[r][c] == "1":
                    numIslands += 1
                    visitIslandDFS(r,c)

        return numIslands
    