class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix) - 1, len(matrix[0])
        ret = []
        r, c = 0, -1
        
        def helper(dr, dc, dist):
            nonlocal r, c
            for i in range(dist):
                r += dr
                c += dc
                ret.append(matrix[r][c])

        sign = 1
        while (row > 0 and col > 0):
            helper(0, 1 * sign, col)
            col -= 1
            helper(1 * sign, 0, row)
            row -= 1
            sign *= -1
        
        if col > 0:
            helper(0, 1 * sign, col)
        elif row >= 0 and len(ret) < len(matrix) * len(matrix[0]):
            helper(1 * sign, 0, row + 1)

        return ret