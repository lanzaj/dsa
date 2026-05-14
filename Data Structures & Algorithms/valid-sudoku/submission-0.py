class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            count = Counter(board[i])
            count["."] = 0
            #print(count)
            if max(count.values()) > 1:
                return False

        for col in range(9):
            count = defaultdict(int)
            for row in range(9):
                count[board[row][col]] += 1
            count["."] = 0
            #print(count)
            if max(count.values()) > 1:
                return False
        
        for col in range(3):
            for row in range(3):
                count = defaultdict(int)
                for C in range(3):
                    for R in range(3):
                        count[board[row*3+R][col*3+C]] += 1
                count["."] = 0
                #print(count)
                if max(count.values()) > 1:
                    return False

        return True