class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r, l = 0, len(matrix[0]) - 1
        t, b = 0, len(matrix) - 1

        ret = []
        while r <= l and t <= b:
            i = r
            while i <= l:
                ret.append(matrix[t][i])
                i += 1
            t += 1
            
            i = t
            while i <= b:
                ret.append(matrix[i][l])
                i += 1
            l -= 1
            

            if r > l or t > b:
                break 
            i = l
            while i >= r:
                ret.append(matrix[b][i])
                i -= 1
            b -= 1

            i = b
            while i >= t:
                ret.append(matrix[i][r])
                i -= 1
            r += 1

        return ret