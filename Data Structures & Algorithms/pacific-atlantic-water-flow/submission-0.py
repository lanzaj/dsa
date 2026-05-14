class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        for c in range(COLS):
            pacific.add((0, c))
            atlantic.add((ROWS - 1, c))

        for r in range(ROWS):
            pacific.add((r, 0))
            atlantic.add((r, COLS - 1))

        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs_pacific(r, c):
            for d in dir:
                if (r + d[0], c + d[1]) in pacific:
                    continue
                if r + d[0] < 0 or r + d[0] >= ROWS:
                    continue
                if c + d[1] < 0 or c + d[1] >= COLS:
                    continue
                if heights[r][c] <= heights[r + d[0]][c + d[1]]:
                    pacific.add((r + d[0], c + d[1]))
                    dfs_pacific(r + d[0], c + d[1])
        for r, c in pacific.copy():
            dfs_pacific(r, c)

        def dfs_atlantic(r, c):
            for d in dir:
                if (r + d[0], c + d[1]) in atlantic:
                    continue
                if r + d[0] < 0 or r + d[0] >= ROWS:
                    continue
                if c + d[1] < 0 or c + d[1] >= COLS:
                    continue
                if heights[r][c] <= heights[r + d[0]][c + d[1]]:
                    atlantic.add((r + d[0], c + d[1]))
                    dfs_atlantic(r + d[0], c + d[1])
        for r, c in atlantic.copy():
            dfs_atlantic(r, c)
        
        ret = []
        for coord in pacific:
            if coord in atlantic:
                ret.append([coord[0], coord[1]])

        return ret
        

        



