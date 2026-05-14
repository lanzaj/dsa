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
        def dfs(r, c, my_set):
            for d in dir:
                nr, nc = r + d[0], c + d[1]
                if (nr, nc) in my_set or nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                    continue
                if heights[r][c] <= heights[nr][nc]:
                    my_set.add((nr, nc))
                    dfs(nr, nc, my_set)
    
        for r, c in pacific.copy():
            dfs(r, c, pacific)
        for r, c in atlantic.copy():
            dfs(r, c, atlantic)
        
        res = []
        for coord in pacific:
            if coord in atlantic:
                res.append([coord[0], coord[1]])

        return res
        

        



