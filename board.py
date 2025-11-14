"""
Board module for Sudoku Master.
Implements the Board class following OOP principles.
"""

from typing import Optional
from cell import Cell


class Board:
    """
    Represents a 9x9 Sudoku board.

    Responsibility: Manage the entire game board
    - Store 81 Cell objects in a 9x9 grid
    - Provide interface for accessing/modifying cells
    - Encapsulate board state

    OOP Principles Applied:
    - Encapsulation: _cells is private, accessed via methods
    - Single Responsibility: Only manages board structure
    - Dependency Injection: Validator is injected
    """

    def __init__(self):
        """Initialize an empty 9x9 board."""
        # Private: 9x9 grid of Cell objects
        self._cells = [[Cell() for _ in range(9)] for _ in range(9)]
        self._validator = None  # Validator will be injected later

    def set_validator(self, validator) -> None:
        """
        Inject validator dependency.

        Args:
            validator: Validator instance for rule checking
        """
        self._validator = validator

    # Public interface methods

    def get_cell(self, row: int, col: int) -> Cell:
        """
        Get the cell at the specified position.

        Args:
            row: Row index (0-8)
            col: Column index (0-8)

        Returns:
            Cell at the specified position
        """
        return self._cells[row][col]

    def set_cell(self, row: int, col: int, value: int) -> bool:
        """
        Set cell value with validation.

        Args:
            row: Row index (0-8)
            col: Column index (0-8)
            value: New value (0-9)

        Returns:
            True if value was set successfully, False otherwise
        """
        cell = self._cells[row][col]

        if cell.is_given:
            return False  # Cannot modify initial values

        # Validate move if validator is available
        if self._validator and value != 0:
            if not self._validator.is_valid_move(self, row, col, value):
                cell.mark_invalid()
                return False

        cell.set_value(value)
        cell.mark_valid()
        return True

    def clear_cell(self, row: int, col: int) -> None:
        """
        Clear the cell at the specified position.

        Args:
            row: Row index (0-8)
            col: Column index (0-8)
        """
        self._cells[row][col].clear()

    def is_full(self) -> bool:
        """
        Check if the board is completely filled.

        Returns:
            True if no empty cells, False otherwise
        """
        for row in range(9):
            for col in range(9):
                if self._cells[row][col].is_empty:
                    return False
        return True

    def reset(self) -> None:
        """Reset the board, clearing all non-given cells."""
        for row in range(9):
            for col in range(9):
                if not self._cells[row][col].is_given:
                    self._cells[row][col].clear()

    def __repr__(self) -> str:
        """String representation for debugging."""
        lines = []
        for row in range(9):
            line = " ".join(str(self._cells[row][col].value) for col in range(9))
            lines.append(line)
        return "\n".join(lines)
