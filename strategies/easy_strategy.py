"""
Easy difficulty strategy for Sudoku Master.
"""

from strategies.difficulty_strategy import DifficultyStrategy
import config


class EasyStrategy(DifficultyStrategy):
    """
    Easy difficulty strategy.

    Difficulty Characteristics:
    - Removes 40 cells (provides 41 cells)
    - About 50% of board is given
    - Can be solved with basic techniques
    - Good for beginners
    """

    def get_cells_to_remove(self) -> int:
        """
        Get number of cells to remove for easy difficulty.

        Returns:
            40 cells to remove (41 cells remain)
        """
        return config.EASY_CELLS_TO_REMOVE

    def get_name(self) -> str:
        """
        Get difficulty name.

        Returns:
            "Easy"
        """
        return "Easy"
