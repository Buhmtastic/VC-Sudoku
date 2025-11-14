"""
SetCellCommand module for Sudoku Master.
Implements concrete command for setting a cell value.
"""

from typing import TYPE_CHECKING
from commands.command import Command

if TYPE_CHECKING:
    from board import Board


class SetCellCommand(Command):
    """
    Command to set a cell value.

    Responsibility: Encapsulate setting a cell value as a reversible action

    OOP Principles Applied:
    - Command Pattern: Encapsulates action as object
    - Encapsulation: Stores old and new values privately
    - Single Responsibility: Only handles setting cell value

    Attributes:
        _board: The game board
        _row: Row index of the cell
        _col: Column index of the cell
        _new_value: New value to set
        _old_value: Previous value (for undo)
    """

    def __init__(self, board: 'Board', row: int, col: int, new_value: int):
        """
        Initialize SetCellCommand.

        Args:
            board: The game board
            row: Row index (0-8)
            col: Column index (0-8)
            new_value: New value to set (1-9)
        """
        self._board = board
        self._row = row
        self._col = col
        self._new_value = new_value

        # Store old value for undo
        cell = self._board.get_cell(row, col)
        self._old_value = cell.value

    def execute(self) -> None:
        """
        Execute the command: set the cell value.

        Sets the cell at (row, col) to the new value.
        Validation is performed by the Board class.
        """
        self._board.set_cell(self._row, self._col, self._new_value)

    def undo(self) -> None:
        """
        Undo the command: restore the old cell value.

        Restores the cell to its previous value.
        If old value was 0 (empty), the cell is cleared.
        """
        if self._old_value == 0:
            self._board.clear_cell(self._row, self._col)
        else:
            self._board.set_cell(self._row, self._col, self._old_value)

    def get_description(self) -> str:
        """
        Get command description.

        Returns:
            str: Human-readable description of the command
        """
        return f"Set cell ({self._row}, {self._col}) to {self._new_value}"
