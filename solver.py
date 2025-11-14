"""
Solver module for Sudoku Master.
Implements the Solver class using backtracking algorithm.
"""

from typing import Optional, Tuple


class Solver:
    """
    Solves Sudoku puzzles using backtracking algorithm.

    Responsibility: Find solution to Sudoku puzzle
    - Implement backtracking algorithm
    - Find empty cells
    - Check for unique solutions

    OOP Principles Applied:
    - Single Responsibility: Only handles puzzle solving
    - Dependency Injection: Requires Validator
    - Encapsulation: Algorithm details hidden
    """

    def __init__(self, validator):
        """
        Initialize solver with validator dependency.

        Args:
            validator: Validator instance for checking moves
        """
        self._validator = validator

    def solve(self, board) -> bool:
        """
        Solve the Sudoku board using backtracking.

        Algorithm:
        1. Find empty cell
        2. Try numbers 1-9
        3. If valid, place number and recurse
        4. If recursion succeeds, done
        5. Otherwise, backtrack and try next number

        Args:
            board: Board instance to solve

        Returns:
            True if solved, False if no solution exists
        """
        empty_cell = self._find_empty_cell(board)

        if not empty_cell:
            return True  # Board is complete

        row, col = empty_cell

        # Try numbers 1-9
        for num in range(1, 10):
            if self._validator.is_valid_move(board, row, col, num):
                # Place number
                board.set_cell(row, col, num)

                # Recursively solve
                if self.solve(board):
                    return True

                # Backtrack if solution not found
                board.clear_cell(row, col)

        return False  # No solution found

    def has_unique_solution(self, board) -> bool:
        """
        Check if the board has exactly one solution.

        Args:
            board: Board instance to check

        Returns:
            True if exactly one solution exists, False otherwise

        Note: This is a placeholder. Full implementation would count solutions.
        """
        # TODO: Implement solution counting in Phase 3
        return True

    # Private methods

    def _find_empty_cell(self, board) -> Optional[Tuple[int, int]]:
        """
        Find the first empty cell in the board.

        Args:
            board: Board instance

        Returns:
            Tuple of (row, col) if empty cell found, None otherwise
        """
        for row in range(9):
            for col in range(9):
                if board.get_cell(row, col).is_empty:
                    return (row, col)
        return None
