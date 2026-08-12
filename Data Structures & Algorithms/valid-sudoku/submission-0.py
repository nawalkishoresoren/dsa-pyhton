class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        grid = defaultdict(set)

        for row in range(9):
            for col in range(9):
                val = board[row][col]

                if val == ".":
                    continue
                
                grid_no = (row//3)*3 + (col//3)

                if val in rows[row] or val in columns[col] or val in grid[grid_no]:
                    return False
                
                rows[row].add(val)
                columns[col].add(val)
                grid[grid_no].add(val)

        return True
        