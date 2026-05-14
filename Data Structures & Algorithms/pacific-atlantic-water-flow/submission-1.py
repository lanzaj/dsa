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
                if (r + d[0], c + d[1]) in my_set:
                    continue
                if r + d[0] < 0 or r + d[0] >= ROWS:
                    continue
                if c + d[1] < 0 or c + d[1] >= COLS:
                    continue
                if heights[r][c] <= heights[r + d[0]][c + d[1]]:
                    my_set.add((r + d[0], c + d[1]))
                    dfs(r + d[0], c + d[1], my_set)
    
        for r, c in pacific.copy():
            dfs(r, c, pacific)
        for r, c in atlantic.copy():
            dfs(r, c, atlantic)
        
        ret = []
        for coord in pacific:
            if coord in atlantic:
                ret.append([coord[0], coord[1]])

        return ret
        

        



