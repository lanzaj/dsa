class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        def helper(r, c, dr, dc):
            while r >= 0 and r < ROWS and \
                c >= 0 and c < COLS:
                if matrix[r][c] != 0:
                    matrix[r][c] = 0
                r += dr
                c += dc

        # Mark cols and rows to erase in the first col / row
        # Use col0 to encode the first col as (0, 0) already encode first row
        col0 = 1
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    if c == 0:
                        col0 = 0
                    else:
                        matrix[0][c] = 0
                    matrix[r][0] = 0
        
        # Fill rows and cols with 0
        for c in range(1, COLS):
            if matrix[0][c] == 0:
                helper(0, c, 1, 0) 
        for r in range(ROWS):
            if matrix[r][0] == 0:
                helper(r, 0, 0, 1)
        if col0 == 0:
            helper(0, 0, 1, 0) 
        