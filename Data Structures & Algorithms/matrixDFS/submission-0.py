class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        COL, ROW = len(grid), len(grid[0])
        visited = set()

        def dfs(row: int, col:int) ->int:
            if (min(row, col) < 0
                or row >= ROW
                or col >= COL 
                or (row, col) in visited
                or grid[col][row]):
                return 0
            if row == ROW - 1 and col == COL -1:
                return 1
            
            visited.add((row, col))

            count = 0
            count += dfs(row-1, col)
            count += dfs(row, col-1)
            count += dfs(row+1, col)
            count += dfs(row, col+1)

            visited.remove((row, col))
            return count
        
        return dfs(0, 0)