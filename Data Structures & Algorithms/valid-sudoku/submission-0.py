class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] in s:
                    return False
                elif board[i][j] != '.':
                    s.add(board[i][j])
 
        # check cols
        for i in range(9):
            s = set()
            for j in range(9):
                if board[j][i] in s:
                    return False
                elif board[j][i] != '.':
                    s.add(board[j][i])

        # check boxes
        starts = [(0,0), (0,3), (0,6),
        (3,0), (3,3), (3,6),
        (6,0), (6,3), (6,6)]

        for i, j in starts:
            s = set()
            for n in range(i, i+3):
                for k in range(j, j+3):
                    if board[n][k] in s:
                        return False
                    elif board[n][k] != '.':
                        s.add(board[n][k])
        return True
