"""
Game module for Sudoku Master.
Implements the Game class - main game controller.
"""

import pygame
from typing import Optional, Tuple
import config
from board import Board
from cell import Cell
from validator import Validator
from ui.renderer import Renderer


class Game:
    """
    Main game controller for Sudoku Master.

    Responsibility: Manage game flow and components
    - Initialize PyGame
    - Run game loop
    - Handle events
    - Coordinate all game components

    OOP Principles Applied:
    - Single Responsibility: Game flow management
    - Dependency Injection: Components created and injected
    - Facade Pattern: Simplifies interaction with subsystems
    """

    def __init__(self):
        """Initialize the game."""
        # Initialize PyGame
        pygame.init()

        # Create display
        self._screen = pygame.display.set_mode(
            (config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
        )
        pygame.display.set_caption("Sudoku Master")

        # Create clock for FPS control
        self._clock = pygame.time.Clock()

        # Game state
        self._running = False
        self._selected_cell: Optional[Tuple[int, int]] = None

        # Create game components (Dependency Injection)
        self._board = Board()
        self._validator = Validator()
        self._board.set_validator(self._validator)
        self._renderer = Renderer(self._screen)

        # Initialize with empty board for now
        # TODO: In Phase 3, generate puzzle here
        self._init_test_board()

    def _init_test_board(self) -> None:
        """
        Initialize a test board with some numbers.
        This is temporary for Phase 1 testing.
        Will be replaced with puzzle generation in Phase 3.
        """
        # Add a few test numbers to verify rendering
        test_values = [
            (0, 0, 5), (0, 1, 3), (0, 4, 7),
            (1, 0, 6), (1, 3, 1), (1, 4, 9), (1, 5, 5),
            (2, 1, 9), (2, 2, 8), (2, 7, 6),
            (3, 0, 8), (3, 4, 6), (3, 8, 3),
            (4, 0, 4), (4, 3, 8), (4, 5, 3), (4, 8, 1),
            (5, 0, 7), (5, 4, 2), (5, 8, 6),
            (6, 1, 6), (6, 6, 2), (6, 7, 8),
            (7, 3, 4), (7, 4, 1), (7, 5, 9), (7, 8, 5),
            (8, 4, 8), (8, 7, 7), (8, 8, 9),
        ]

        for row, col, value in test_values:
            cell = self._board.get_cell(row, col)
            cell._value = value
            cell._is_given = True  # Mark as initial values

    def run(self) -> None:
        """
        Run the main game loop.

        Game Loop:
        1. Handle events (input)
        2. Update game state
        3. Render frame
        4. Control FPS
        """
        self._running = True

        while self._running:
            # Handle events
            self._handle_events()

            # Update game state
            self._update()

            # Render frame
            self._render()

            # Control frame rate
            self._clock.tick(config.FPS)

        # Clean up
        pygame.quit()

    def _handle_events(self) -> None:
        """Handle user input events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False

            elif event.type == pygame.KEYDOWN:
                self._handle_keypress(event.key)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._handle_mouse_click(event.pos)

    def _handle_keypress(self, key: int) -> None:
        """
        Handle keyboard input.

        Args:
            key: PyGame key code
        """
        # ESC to quit
        if key == pygame.K_ESCAPE:
            self._running = False

        # Number keys 1-9
        elif pygame.K_1 <= key <= pygame.K_9:
            if self._selected_cell:
                row, col = self._selected_cell
                number = key - pygame.K_0  # Convert key code to number
                self._place_number(row, col, number)

        # Delete/Backspace to clear cell
        elif key in (pygame.K_DELETE, pygame.K_BACKSPACE):
            if self._selected_cell:
                row, col = self._selected_cell
                self._clear_cell(row, col)

        # Arrow keys for navigation (bonus feature)
        elif key == pygame.K_UP:
            self._move_selection(0, -1)
        elif key == pygame.K_DOWN:
            self._move_selection(0, 1)
        elif key == pygame.K_LEFT:
            self._move_selection(-1, 0)
        elif key == pygame.K_RIGHT:
            self._move_selection(1, 0)

    def _handle_mouse_click(self, pos: Tuple[int, int]) -> None:
        """
        Handle mouse click events.

        Args:
            pos: Mouse position (x, y)
        """
        # Convert mouse position to cell coordinates
        cell_pos = self._renderer.get_cell_from_pos(pos)

        if cell_pos:
            self._selected_cell = cell_pos

    def _place_number(self, row: int, col: int, number: int) -> None:
        """
        Place a number in the specified cell.

        Args:
            row: Row index (0-8)
            col: Column index (0-8)
            number: Number to place (1-9)
        """
        success = self._board.set_cell(row, col, number)

        if success:
            # Check if board is solved
            if self._validator.is_board_solved(self._board):
                print("Congratulations! Puzzle solved!")  # TODO: Show UI message in Phase 5
        else:
            print(f"Invalid move: Cannot place {number} at ({row}, {col})")

    def _clear_cell(self, row: int, col: int) -> None:
        """
        Clear the specified cell.

        Args:
            row: Row index (0-8)
            col: Column index (0-8)
        """
        self._board.clear_cell(row, col)

    def _move_selection(self, dx: int, dy: int) -> None:
        """
        Move cell selection by delta.

        Args:
            dx: Column delta (-1, 0, 1)
            dy: Row delta (-1, 0, 1)
        """
        if self._selected_cell:
            row, col = self._selected_cell
            new_row = max(0, min(8, row + dy))
            new_col = max(0, min(8, col + dx))
            self._selected_cell = (new_row, new_col)
        else:
            # If nothing selected, select center cell
            self._selected_cell = (4, 4)

    def _update(self) -> None:
        """Update game state."""
        # TODO: Add timer update in Phase 4
        # TODO: Add animation updates in Phase 5
        pass

    def _render(self) -> None:
        """Render the current frame."""
        # Render board
        self._renderer.render_board(self._board, self._selected_cell)

        # Render UI elements
        self._renderer.render_ui(timer_text="00:00")  # TODO: Real timer in Phase 4

        # Update display
        pygame.display.flip()
