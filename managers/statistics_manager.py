"""
StatisticsManager module for Sudoku Master.
Implements game statistics tracking.
"""


class StatisticsManager:
    """
    Manages game statistics.

    Responsibility: Track and report game statistics

    OOP Principles Applied:
    - Single Responsibility: Only manages statistics
    - Encapsulation: Statistics are private

    Tracks:
    - Number of moves (cell placements)
    - Number of undos
    - Number of redos
    - Number of hints used
    - Invalid move attempts

    Attributes:
        _moves: Number of cell placements
        _undos: Number of undo operations
        _redos: Number of redo operations
        _hints_used: Number of hints used
        _invalid_moves: Number of invalid move attempts
    """

    def __init__(self):
        """Initialize StatisticsManager with zero statistics."""
        self._moves: int = 0
        self._undos: int = 0
        self._redos: int = 0
        self._hints_used: int = 0
        self._invalid_moves: int = 0

    def record_move(self) -> None:
        """Record a cell placement move."""
        self._moves += 1

    def record_undo(self) -> None:
        """Record an undo operation."""
        self._undos += 1

    def record_redo(self) -> None:
        """Record a redo operation."""
        self._redos += 1

    def record_hint(self) -> None:
        """Record a hint usage."""
        self._hints_used += 1

    def record_invalid_move(self) -> None:
        """Record an invalid move attempt."""
        self._invalid_moves += 1

    def reset(self) -> None:
        """Reset all statistics to zero."""
        self._moves = 0
        self._undos = 0
        self._redos = 0
        self._hints_used = 0
        self._invalid_moves = 0

    @property
    def moves(self) -> int:
        """
        Get number of moves.

        Returns:
            int: Total number of cell placements
        """
        return self._moves

    @property
    def undos(self) -> int:
        """
        Get number of undos.

        Returns:
            int: Total number of undo operations
        """
        return self._undos

    @property
    def redos(self) -> int:
        """
        Get number of redos.

        Returns:
            int: Total number of redo operations
        """
        return self._redos

    @property
    def hints_used(self) -> int:
        """
        Get number of hints used.

        Returns:
            int: Total number of hints used
        """
        return self._hints_used

    @property
    def invalid_moves(self) -> int:
        """
        Get number of invalid moves.

        Returns:
            int: Total number of invalid move attempts
        """
        return self._invalid_moves

    def get_total_actions(self) -> int:
        """
        Get total number of actions.

        Returns:
            int: Sum of moves, undos, and redos
        """
        return self._moves + self._undos + self._redos

    def get_summary(self) -> str:
        """
        Get formatted statistics summary.

        Returns:
            str: Multi-line summary of statistics
        """
        return (
            f"Moves: {self._moves}\n"
            f"Undos: {self._undos}\n"
            f"Redos: {self._redos}\n"
            f"Hints: {self._hints_used}\n"
            f"Invalid Moves: {self._invalid_moves}\n"
            f"Total Actions: {self.get_total_actions()}"
        )
