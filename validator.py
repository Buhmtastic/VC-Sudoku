"""
Validator module for Sudoku Master.
Implements the Validator class following OOP principles.
"""


class Validator:
    """
    Validates Sudoku rules.

    Responsibility: Check if moves follow Sudoku rules
    - Validate row uniqueness
    - Validate column uniqueness
    - Validate 3x3 box uniqueness
    - Check if board is solved

    OOP Principles Applied:
    - Single Responsibility: Only handles validation
    - Encapsulation: Internal logic in private methods
    - Method Separation: Each check is independent
    """

    def is_valid_move(self, board, row: int, col: int, num: int) -> bool:
        """
        Check if placing a number is valid.

        Args:
            board: Board instance
            row: Row index (0-8)
            col: Column index (0-8)
            num: Number to place (1-9)

        Returns:
            True if move is valid, False otherwise
        """
        if num == 0:  # Empty cell is always valid
            return True

        return (self._check_row(board, row, num, col) and
                self._check_column(board, col, num, row) and
                self._check_box(board, row, col, num))

    def is_board_solved(self, board) -> bool:
        """
        Check if the board is completely and correctly solved.

        Args:
            board: Board instance

        Returns:
            True if board is solved, False otherwise
        """
        if not board.is_full():
            return False

        # Check all cells are valid
        for row in range(9):
            for col in range(9):
                cell = board.get_cell(row, col)
                if not cell.is_valid:
                    return False

        return True

    # Private validation methods

    def _check_row(self, board, row: int, num: int, skip_col: int = -1) -> bool:
        """
        Check if number exists in the row.

        Args:
            board: Board instance
            row: Row index to check
            num: Number to check
            skip_col: Column to skip (current cell)

        Returns:
            True if number doesn't exist in row, False otherwise
        """
        for col in range(9):
            if col == skip_col:
                continue
            cell = board.get_cell(row, col)
            if cell.value == num:
                return False
        return True

    def _check_column(self, board, col: int, num: int, skip_row: int = -1) -> bool:
        """
        Check if number exists in the column.

        Args:
            board: Board instance
            col: Column index to check
            num: Number to check
            skip_row: Row to skip (current cell)

        Returns:
            True if number doesn't exist in column, False otherwise
        """
        for row in range(9):
            if row == skip_row:
                continue
            cell = board.get_cell(row, col)
            if cell.value == num:
                return False
        return True

    def _check_box(self, board, row: int, col: int, num: int) -> bool:
        """
        Check if number exists in the 3x3 box.

        Args:
            board: Board instance
            row: Row index of cell
            col: Column index of cell
            num: Number to check

        Returns:
            True if number doesn't exist in box, False otherwise
        """
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3

        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if r == row and c == col:
                    continue
                cell = board.get_cell(r, c)
                if cell.value == num:
                    return False
        return True
