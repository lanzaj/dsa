class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0] or grid[0][0] == 1:
            return -1
        queue = deque()
        ROW, COL = len(grid), len(grid[0])
        queue.append((0,0,0))
        
        dir = [[0,1], [-1,0], [0,-1], [1,0]]
        while queue:
            r, c,shortestPathLen = queue.popleft()
            if r == ROW - 1 and c == COL - 1:
                return shortestPathLen
            for dr, dc in dir:
                curR, curC = r + dr, c + dc
                if (min(curR, curC) < 0
                    or curR >= ROW
                    or curC >= COL
                    or grid[curR][curC] != 0):
                    continue
                grid[curR][curC] = 2
                queue.append((curR,curC,shortestPathLen + 1))
        
        return -1
        