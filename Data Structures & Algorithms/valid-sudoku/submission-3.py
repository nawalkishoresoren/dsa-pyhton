class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        grids = defaultdict(set)

        for row in range(9):
            for col in range(9):

                val = board[row][col]

                if val == ".":
                    continue
                
                grid = (row//3)*3 + (col//3)
                if val in rows[row] or val in cols[col] or val in grids[grid]:
                    return False
                
                rows[row].add(val)
                cols[col].add(val)
                grids[grid].add(val)
        
        return True
        