class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        nbRows, nbColumns = len(grid), len(grid[0])
        visit=set()
        islands=0
        def dfs( pos_r, pos_c):
            if (
                pos_r not in range(nbRows)
                or pos_c not in range(nbColumns)
                or (pos_r,pos_c) in visit
                or grid[pos_r][pos_c]=="0"):
                return 
            visit.add((pos_r,pos_c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(pos_r+dr, pos_c+dc)
        
        for r in range(nbRows):
            for c in range(nbColumns):
                if grid[r][c]=="1" and (r,c) not in visit:
                    islands+=1
                    dfs(r,c)
        return islands