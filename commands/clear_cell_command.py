"""
ClearCellCommand module for Sudoku Master.
Implements concrete command for clearing a cell value.
"""

from typing import TYPE_CHECKING
from commands.command import Command

if TYPE_CHECKING:
    from board import Board


class ClearCellCommand(Command):
    """
    Command to clear a cell value.

    Responsibility: Encapsulate clearing a cell value as a reversible action

    OOP Principles Applied:
    - Command Pattern: Encapsulates action as object
    - Encapsulation: Stores old value privately
    - Single Responsibility: Only handles clearing cell value

    Attributes:
        _board: The game board
        _row: Row index of the cell
        _col: Column index of the cell
        _old_value: Previous value (for undo)
    """

    def __init__(self, board: 'Board', row: int, col: int):
        """
        Initialize ClearCellCommand.

        Args:
            board: The game board
            row: Row index (0-8)
            col: Column index (0-8)
        """
        self._board = board
        self._row = row
        self._col = col

        # Store old value for undo
        cell = self._board.get_cell(row, col)
        self._old_value = cell.value

    def execute(self) -> None:
        """
        Execute the command: clear the cell value.

        Sets the cell at (row, col) to empty (0).
        Only clears if the cell is not a given value.
        """
        self._board.clear_cell(self._row, self._col)

    def undo(self) -> None:
        """
        Undo the command: restore the old cell value.

        Restores the cell to its previous value.
        If old value was 0, the cell remains empty (no change).
        """
        if self._old_value != 0:
            self._board.set_cell(self._row, self._col, self._old_value)

    def get_description(self) -> str:
        """
        Get command description.

        Returns:
            str: Human-readable description of the command
        """
        return f"Clear cell ({self._row}, {self._col})"
