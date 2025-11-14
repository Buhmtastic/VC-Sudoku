"""
Difficulty Strategy module for Sudoku Master.
Implements the Strategy Pattern for difficulty levels.
"""

from abc import ABC, abstractmethod


class DifficultyStrategy(ABC):
    """
    Abstract base class for difficulty strategies.

    Responsibility: Define interface for difficulty levels
    - Specify how many cells to remove for each difficulty
    - Allow easy addition of new difficulty levels

    OOP Principles Applied:
    - Strategy Pattern: Encapsulate difficulty algorithms
    - Open/Closed Principle: Open for extension, closed for modification
    - Polymorphism: All strategies share same interface
    """

    @abstractmethod
    def get_cells_to_remove(self) -> int:
        """
        Get the number of cells to remove for this difficulty.

        Returns:
            Number of cells to remove from completed board

        Note:
            81 total cells in 9x9 Sudoku board
            More removals = harder puzzle
        """
        pass

    @abstractmethod
    def get_name(self) -> str:
        """
        Get the display name of this difficulty.

        Returns:
            Human-readable difficulty name
        """
        pass

    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"{self.__class__.__name__}(remove={self.get_cells_to_remove()}, name='{self.get_name()}')"
