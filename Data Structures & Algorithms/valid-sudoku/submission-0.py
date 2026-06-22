from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid(board, indices):
            dic = defaultdict(bool)
            for row, col in indices:
                if board[row][col] != '.':
                    if dic[board[row][col]]:
                        return False
                    dic[board[row][col]] = True
            return True

        def get_square(row_offset, col_offset):
            return (
                [[row_offset, col_offset+i] for i in range(3)] +
                [[row_offset+1, col_offset+i] for i in range(3)] +
                [[row_offset+2, col_offset+i] for i in range(3)]
            )
       
        rowwise = [
            [[row, col] for col in range(9)]
            for row in range(9)
        ]
        colwise = [
            [[row, col] for row in range(9)]
            for col in range(9)
        ]
        squarewise = []
        for row_offset in [0, 3, 6]:
            for col_offset in [0, 3, 6]:
                squarewise.append(get_square(row_offset, col_offset))
        # print(squarewise)
        
        for li in [rowwise, colwise, squarewise]:
            for indices in li:
                if not is_valid(board, indices):
                    # print(indices)
                    return False
        return True