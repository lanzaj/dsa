class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0] or grid[0][0] == 1:
            return -1
        queue = deque()
        N = len(grid)
        queue.append((0,0,0))
        
        dir = [[0,1], [-1,0], [0,-1], [1,0]]
        while queue:
            r, c,shortestPathLen = queue.popleft()
            if r == N - 1 and c == N - 1:
                return shortestPathLen
            for dr, dc in dir:
                curR, curC = r + dr, c + dc
                if (min(curR, curC) < 0
                    or max(curR, curC) >= N
                    or grid[curR][curC] != 0):
                    continue
                grid[curR][curC] = 2
                queue.append((curR,curC,shortestPathLen + 1))
        
        return -1
        