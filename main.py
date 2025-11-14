"""
Sudoku Master - Main Entry Point
A professionally crafted Sudoku game demonstrating OOP principles.
"""

from game import Game


def main():
    """Main entry point for the Sudoku game."""
    try:
        # Create and run the game
        game = Game()
        game.run()
    except Exception as e:
        print(f"Error running game: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
