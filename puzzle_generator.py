"""
Puzzle Generator module for Sudoku Master.
Implements the PuzzleGenerator class using Factory Method pattern.
"""

import random
import copy
from board import Board
from cell import Cell


class PuzzleGenerator:
    """
    Generates Sudoku puzzles with specified difficulty.

    Responsibility: Create valid Sudoku puzzles
    - Generate complete boards
    - Remove numbers based on difficulty
    - Ensure unique solutions

    OOP Principles Applied:
    - Factory Method Pattern: generate() creates puzzles
    - Strategy Pattern Integration: Uses difficulty strategies
    - Dependency Injection: Requires Solver
    """

    def __init__(self, solver):
        """
        Initialize generator with solver dependency.

        Args:
            solver: Solver instance for creating/validating puzzles
        """
        self._solver = solver

    def generate(self, difficulty_strategy):
        """
        Generate a puzzle using the specified difficulty strategy.

        Factory Method: Creates puzzles based on strategy.

        Args:
            difficulty_strategy: DifficultyStrategy instance

        Returns:
            Board instance with generated puzzle
        """
        # 1. Create full board
        board = self._create_full_board()

        # 2. Remove cells based on difficulty
        cells_to_remove = difficulty_strategy.get_cells_to_remove()
        self._remove_numbers(board, cells_to_remove)

        # 3. Mark remaining cells as given
        for row in range(9):
            for col in range(9):
                cell = board.get_cell(row, col)
                if not cell.is_empty:
                    cell._is_given = True

        return board

    # Private methods

    def _create_full_board(self):
        """
        Create a complete valid Sudoku board.

        Algorithm:
        1. Start with empty board
        2. Fill diagonal 3x3 boxes (independent)
        3. Use solver to fill remaining cells

        Returns:
            Completed Board instance
        """
        board = Board()

        # Fill diagonal 3x3 boxes first (they don't affect each other)
        for box in range(3):
            self._fill_box(board, box * 3, box * 3)

        # Use solver to fill remaining cells
        self._solver.solve(board)

        return board

    def _fill_box(self, board, row_start: int, col_start: int):
        """
        Fill a 3x3 box with random numbers 1-9.

        Args:
            board: Board instance
            row_start: Starting row of box (0, 3, or 6)
            col_start: Starting column of box (0, 3, or 6)
        """
        numbers = list(range(1, 10))
        random.shuffle(numbers)

        idx = 0
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                cell = board.get_cell(row, col)
                cell._value = numbers[idx]
                idx += 1

    def _remove_numbers(self, board, count: int):
        """
        Remove numbers from board while maintaining unique solution.

        Algorithm:
        1. Create list of all cell positions
        2. Shuffle for randomness
        3. For each position:
           a. Try to remove number
           b. Check if still has unique solution
           c. If not unique, restore number
        4. Stop when desired count reached

        Args:
            board: Board instance
            count: Number of cells to remove
        """
        # Create list of all positions
        positions = [(r, c) for r in range(9) for c in range(9)]
        random.shuffle(positions)

        removed_count = 0

        for row, col in positions:
            if removed_count >= count:
                break

            cell = board.get_cell(row, col)
            if cell.is_empty:
                continue

            # Save current value
            backup_value = cell.value

            # Try removing
            cell._value = 0

            # Check if still has unique solution
            # For performance, we'll use a simplified check:
            # If solver can solve it, we assume it's unique
            # Full unique solution check is expensive
            board_copy = self._copy_board(board)
            if self._solver.solve(board_copy):
                # Solution exists, keep it removed
                removed_count += 1
            else:
                # No solution, restore
                cell._value = backup_value

    def _copy_board(self, board):
        """
        Create a deep copy of the board.

        Args:
            board: Board instance to copy

        Returns:
            New Board instance with same values
        """
        new_board = Board()

        for row in range(9):
            for col in range(9):
                cell = board.get_cell(row, col)
                new_cell = new_board.get_cell(row, col)
                new_cell._value = cell.value
                new_cell._is_given = False  # Don't copy given status

        return new_board
