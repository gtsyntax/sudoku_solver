class Solution:
    def find_next_empty(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    return row, col

        return None, None

    def is_valid(self, board, guess, row, col):
        row_values = board[row]
        if str(guess) in row_values:
            return False

        col_values = [board[row][col] for row in range(9)]
        if str(guess) in col_values:
            return False

        row_start = (row // 3) * 3
        col_start = (col // 3) * 3

        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                if board[row][col] == str(guess):
                    return False

        return True

    def solve_sudoku(self, board):
        """
        Do not return anything, modify board in-place
        """
        # using tuple unpacking to get the next empty cell
        row, col = self.find_next_empty(board)

        if row is None:
            return board

        # try guesses from 1-9
        for guess in range(1, 10):
            if self.is_valid(board, guess, row, col):
                board[row][col] = str(guess)
                if self.solve_sudoku(board):
                    return True
            board[row][col] = "."

        return False


if __name__ == "__main__":
    board_example = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    s1 = Solution()
    s1.solve_sudoku(board_example)
    print(board_example)
