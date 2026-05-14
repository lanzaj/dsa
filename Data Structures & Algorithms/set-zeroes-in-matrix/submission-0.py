class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])

        def helper(r, c, dr, dc):
            r += dr
            c += dc
            while r >= 0 and r < ROWS and \
                c >= 0 and c < COLS:
                if matrix[r][c] != 0:
                    matrix[r][c] = None
                r += dr
                c += dc
            
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    helper(r, c, 1, 0)
                    helper(r, c, -1, 0)
                    helper(r, c, 0, 1)
                    helper(r, c, 0, -1)
                    continue

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == None:
                    matrix[r][c] = 0
        