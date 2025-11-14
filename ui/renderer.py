"""
Renderer module for Sudoku Master.
Implements the Renderer class for drawing the game UI.
"""

import pygame
from typing import Optional, Tuple
import config


class Renderer:
    """
    Renders the Sudoku game UI.

    Responsibility: Draw all visual elements
    - Draw 9x9 grid with borders
    - Draw cell numbers
    - Highlight selected cell
    - Draw UI elements (buttons, timer, etc.)

    OOP Principles Applied:
    - Single Responsibility: Only handles rendering
    - Encapsulation: Drawing logic is private
    - No game state management (read-only access)
    """

    def __init__(self, screen: pygame.Surface):
        """
        Initialize the renderer.

        Args:
            screen: PyGame surface to draw on
        """
        self._screen = screen
        self._font_cell = None
        self._font_ui = None
        self._init_fonts()

    def _init_fonts(self) -> None:
        """Initialize fonts for rendering."""
        pygame.font.init()
        self._font_cell = pygame.font.Font(None, config.FONT_SIZE_CELL)
        self._font_ui = pygame.font.Font(None, config.FONT_SIZE_UI)

    # Public rendering methods

    def render_board(self, board, selected_cell: Optional[Tuple[int, int]] = None) -> None:
        """
        Render the complete board.

        Args:
            board: Board instance to render
            selected_cell: Tuple of (row, col) for selected cell, or None
        """
        self._clear_screen()
        self._draw_grid()
        self._draw_cells(board, selected_cell)
        self._draw_numbers(board)

    def render_ui(self, timer_text: str = "00:00") -> None:
        """
        Render UI elements (timer, buttons, etc.).

        Args:
            timer_text: Timer display text
        """
        self._draw_timer(timer_text)
        # TODO: Add more UI elements in later phases

    # Private drawing methods

    def _clear_screen(self) -> None:
        """Clear the screen with background color."""
        self._screen.fill(config.BG_COLOR)

    def _draw_grid(self) -> None:
        """Draw the 9x9 Sudoku grid with thick box borders."""
        # Draw thin lines for cells
        for i in range(10):
            line_width = config.THIN_LINE_WIDTH

            # Make every 3rd line thick for 3x3 boxes
            if i % 3 == 0:
                line_width = config.THICK_LINE_WIDTH

            # Horizontal lines
            start_x = config.BOARD_OFFSET_X
            end_x = config.BOARD_OFFSET_X + config.CELL_SIZE * 9
            y = config.BOARD_OFFSET_Y + i * config.CELL_SIZE
            pygame.draw.line(
                self._screen,
                config.GRID_COLOR,
                (start_x, y),
                (end_x, y),
                line_width
            )

            # Vertical lines
            start_y = config.BOARD_OFFSET_Y
            end_y = config.BOARD_OFFSET_Y + config.CELL_SIZE * 9
            x = config.BOARD_OFFSET_X + i * config.CELL_SIZE
            pygame.draw.line(
                self._screen,
                config.GRID_COLOR,
                (x, start_y),
                (x, end_y),
                line_width
            )

    def _draw_cells(self, board, selected_cell: Optional[Tuple[int, int]]) -> None:
        """
        Draw cell backgrounds (highlighting).

        Args:
            board: Board instance
            selected_cell: Currently selected cell (row, col) or None
        """
        for row in range(9):
            for col in range(9):
                cell = board.get_cell(row, col)

                # Determine cell color
                color = None
                if selected_cell and selected_cell == (row, col):
                    color = config.CELL_SELECTED_COLOR
                elif not cell.is_valid:
                    color = config.CELL_INVALID_COLOR

                # Draw colored rectangle if needed
                if color:
                    x = config.BOARD_OFFSET_X + col * config.CELL_SIZE
                    y = config.BOARD_OFFSET_Y + row * config.CELL_SIZE
                    rect = pygame.Rect(x, y, config.CELL_SIZE, config.CELL_SIZE)
                    pygame.draw.rect(self._screen, color, rect)

    def _draw_numbers(self, board) -> None:
        """
        Draw numbers in cells.

        Args:
            board: Board instance
        """
        for row in range(9):
            for col in range(9):
                cell = board.get_cell(row, col)

                if not cell.is_empty:
                    # Determine number color
                    if cell.is_given:
                        color = config.CELL_GIVEN_COLOR
                    else:
                        color = config.CELL_USER_COLOR

                    # Render number text
                    text_surface = self._font_cell.render(
                        str(cell.value),
                        True,
                        color
                    )

                    # Center text in cell
                    text_rect = text_surface.get_rect()
                    text_rect.center = (
                        config.BOARD_OFFSET_X + col * config.CELL_SIZE + config.CELL_SIZE // 2,
                        config.BOARD_OFFSET_Y + row * config.CELL_SIZE + config.CELL_SIZE // 2
                    )

                    self._screen.blit(text_surface, text_rect)

    def _draw_timer(self, timer_text: str) -> None:
        """
        Draw timer display.

        Args:
            timer_text: Timer text to display (e.g., "05:23")
        """
        text_surface = self._font_ui.render(
            f"Time: {timer_text}",
            True,
            config.BLACK
        )
        self._screen.blit(text_surface, (config.TIMER_X, config.TIMER_Y))

    def get_cell_from_pos(self, pos: Tuple[int, int]) -> Optional[Tuple[int, int]]:
        """
        Convert mouse position to board cell coordinates.

        Args:
            pos: Mouse position (x, y)

        Returns:
            Tuple of (row, col) if click is on board, None otherwise
        """
        x, y = pos

        # Check if click is within board bounds
        board_x = x - config.BOARD_OFFSET_X
        board_y = y - config.BOARD_OFFSET_Y

        if (0 <= board_x < config.CELL_SIZE * 9 and
            0 <= board_y < config.CELL_SIZE * 9):
            col = board_x // config.CELL_SIZE
            row = board_y // config.CELL_SIZE
            return (row, col)

        return None
