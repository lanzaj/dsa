class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        start, end = 0, len(matrix) - 1

        while start < end:
            for i in range(end - start):
                increasing = start + i
                decreasing = end - i
                matrix[start][increasing], matrix[increasing][end], matrix[end][decreasing], matrix[decreasing][start] = \
                matrix[decreasing][start], matrix[start][increasing], matrix[increasing][end], matrix[end][decreasing]
            start += 1
            end -= 1
