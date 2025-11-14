"""
Medium difficulty strategy for Sudoku Master.
"""

from strategies.difficulty_strategy import DifficultyStrategy
import config


class MediumStrategy(DifficultyStrategy):
    """
    Medium difficulty strategy.

    Difficulty Characteristics:
    - Removes 51 cells (provides 30 cells)
    - About 37% of board is given
    - Requires intermediate techniques
    - Good for regular players
    """

    def get_cells_to_remove(self) -> int:
        """
        Get number of cells to remove for medium difficulty.

        Returns:
            51 cells to remove (30 cells remain)
        """
        return config.MEDIUM_CELLS_TO_REMOVE

    def get_name(self) -> str:
        """
        Get difficulty name.

        Returns:
            "Medium"
        """
        return "Medium"
