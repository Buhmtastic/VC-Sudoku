"""
HintProvider module for Sudoku Master.
Implements hint system for helping players.
"""

from typing import Optional, Tuple
import random
from board import Board
from solver import Solver


class HintProvider:
    """
    Provides hints for Sudoku puzzles.

    Responsibility: Generate hints by finding valid moves

    OOP Principles Applied:
    - Single Responsibility: Only provides hints
    - Dependency Injection: Requires Solver instance
    - Encapsulation: Hint algorithm hidden

    The hint system works by:
    1. Finding all empty cells
    2. Using the solver to determine correct values
    3. Selecting a random empty cell to reveal

    Attributes:
        _solver: Solver instance for determining correct values
    """

    def __init__(self, solver: Solver):
        """
        Initialize HintProvider.

        Args:
            solver: Solver instance for puzzle solving
        """
        self._solver = solver

    def get_hint(self, board: Board) -> Optional[Tuple[int, int, int]]:
        """
        Get a hint for the current board state.

        Args:
            board: Current game board

        Returns:
            Tuple of (row, col, value) if hint available, None otherwise

        Algorithm:
        1. Create a copy of the board
        2. Solve the copy to get the solution
        3. Find all empty cells in the original board
        4. Select a random empty cell
        5. Return the correct value from the solution
        """
        # Find all empty cells
        empty_cells = self._find_empty_cells(board)

        if not empty_cells:
            return None  # No empty cells, puzzle is complete

        # Create a copy of the board for solving
        board_copy = self._copy_board(board)

        # Solve the copy
        if not self._solver.solve(board_copy):
            return None  # Puzzle is unsolvable

        # Select a random empty cell
        row, col = random.choice(empty_cells)

        # Get the correct value from the solved board
        correct_value = board_copy.get_cell(row, col).value

        return (row, col, correct_value)

    def _find_empty_cells(self, board: Board) -> list:
        """
        Find all empty cells in the board.

        Args:
            board: Game board

        Returns:
            List of (row, col) tuples for empty cells
        """
        empty_cells = []

        for row in range(9):
            for col in range(9):
                cell = board.get_cell(row, col)
                if cell.is_empty:
                    empty_cells.append((row, col))

        return empty_cells

    def _copy_board(self, board: Board) -> Board:
        """
        Create a deep copy of the board.

        Args:
            board: Board to copy

        Returns:
            New Board instance with same values
        """
        new_board = Board()

        for row in range(9):
            for col in range(9):
                cell = board.get_cell(row, col)
                if not cell.is_empty:
                    new_cell = new_board.get_cell(row, col)
                    new_cell._value = cell.value
                    new_cell._is_given = cell.is_given

        return new_board

    def count_available_hints(self, board: Board) -> int:
        """
        Count the number of available hints.

        Args:
            board: Current game board

        Returns:
            Number of empty cells (available hints)
        """
        return len(self._find_empty_cells(board))
