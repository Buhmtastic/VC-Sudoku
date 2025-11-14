"""
Hard difficulty strategy for Sudoku Master.
"""

from strategies.difficulty_strategy import DifficultyStrategy
import config


class HardStrategy(DifficultyStrategy):
    """
    Hard difficulty strategy.

    Difficulty Characteristics:
    - Removes 56 cells (provides 25 cells)
    - About 31% of board is given
    - Requires advanced techniques
    - Good for expert players
    """

    def get_cells_to_remove(self) -> int:
        """
        Get number of cells to remove for hard difficulty.

        Returns:
            56 cells to remove (25 cells remain)
        """
        return config.HARD_CELLS_TO_REMOVE

    def get_name(self) -> str:
        """
        Get difficulty name.

        Returns:
            "Hard"
        """
        return "Hard"
