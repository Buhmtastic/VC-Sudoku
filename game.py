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
from solver import Solver
from puzzle_generator import PuzzleGenerator
from strategies.easy_strategy import EasyStrategy
from strategies.medium_strategy import MediumStrategy
from strategies.hard_strategy import HardStrategy
from ui.renderer import Renderer
from ui.button import Button
from managers.command_history import CommandHistory
from managers.hint_provider import HintProvider
from managers.timer import Timer
from managers.statistics_manager import StatisticsManager
from commands.set_cell_command import SetCellCommand
from commands.clear_cell_command import ClearCellCommand


class Game:
    """
    Main game controller for Sudoku Master.

    Responsibility: Manage game flow and components
    - Initialize PyGame
    - Run game loop
    - Handle events
    - Coordinate all game components
    - Manage game states (menu, playing)

    OOP Principles Applied:
    - Single Responsibility: Game flow management
    - Dependency Injection: Components created and injected
    - Facade Pattern: Simplifies interaction with subsystems
    - State Pattern: Different behavior based on game state
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
        self._state = config.STATE_MENU  # Start in menu
        self._selected_cell: Optional[Tuple[int, int]] = None
        self._current_difficulty = None

        # Create game components (Dependency Injection)
        self._validator = Validator()
        self._solver = Solver(self._validator)
        self._generator = PuzzleGenerator(self._solver)
        self._renderer = Renderer(self._screen)

        # Board (will be generated when difficulty selected)
        self._board = None

        # Difficulty strategies
        self._easy_strategy = EasyStrategy()
        self._medium_strategy = MediumStrategy()
        self._hard_strategy = HardStrategy()

        # Command history for Undo/Redo
        self._command_history = CommandHistory()

        # Hint provider
        self._hint_provider = HintProvider(self._solver)

        # Timer for tracking game time
        self._timer = Timer()

        # Statistics manager
        self._statistics = StatisticsManager()

        # Create UI buttons
        self._create_buttons()

    def _create_buttons(self) -> None:
        """Create all UI buttons."""
        button_y = 150
        button_spacing = 60

        # Difficulty buttons (shown in menu)
        self._easy_button = Button(
            200, button_y,
            200, 50,
            "Easy",
            lambda: self._start_game(self._easy_strategy)
        )

        self._medium_button = Button(
            200, button_y + button_spacing,
            200, 50,
            "Medium",
            lambda: self._start_game(self._medium_strategy)
        )

        self._hard_button = Button(
            200, button_y + button_spacing * 2,
            200, 50,
            "Hard",
            lambda: self._start_game(self._hard_strategy)
        )

        # New Game button (shown during play)
        self._new_game_button = Button(
            30, 30,
            120, 40,
            "New Game",
            self._return_to_menu
        )

        # Hint button (shown during play)
        self._hint_button = Button(
            160, 30,
            100, 40,
            "Hint",
            self._use_hint
        )

    def _start_game(self, difficulty_strategy) -> None:
        """
        Start a new game with the specified difficulty.

        Args:
            difficulty_strategy: DifficultyStrategy instance
        """
        print(f"Generating {difficulty_strategy.get_name()} puzzle...")

        # Generate new puzzle
        self._board = self._generator.generate(difficulty_strategy)
        self._board.set_validator(self._validator)

        # Clear command history for new game
        self._command_history.clear()

        # Reset and start timer
        self._timer.start()

        # Reset statistics
        self._statistics.reset()

        # Update state
        self._current_difficulty = difficulty_strategy
        self._state = config.STATE_PLAYING
        self._selected_cell = None

        print("Puzzle generated!")

    def _return_to_menu(self) -> None:
        """Return to main menu."""
        # Stop timer
        self._timer.stop()

        self._state = config.STATE_MENU
        self._board = None
        self._selected_cell = None

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
                if self._state == config.STATE_PLAYING:
                    self._handle_keypress(event.key)
                elif event.type == pygame.K_ESCAPE:
                    self._running = False

            elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
                self._handle_mouse_event(event)

    def _handle_mouse_event(self, event: pygame.event.Event) -> None:
        """
        Handle mouse events (clicks, motion).

        Args:
            event: PyGame mouse event
        """
        if self._state == config.STATE_MENU:
            # Handle difficulty button clicks
            self._easy_button.handle_event(event)
            self._medium_button.handle_event(event)
            self._hard_button.handle_event(event)

        elif self._state == config.STATE_PLAYING:
            # Handle New Game button
            self._new_game_button.handle_event(event)

            # Handle Hint button
            self._hint_button.handle_event(event)

            # Handle cell selection
            if event.type == pygame.MOUSEBUTTONDOWN:
                self._handle_mouse_click(event.pos)

    def _handle_keypress(self, key: int) -> None:
        """
        Handle keyboard input.

        Args:
            key: PyGame key code
        """
        # Check for Ctrl key modifier
        ctrl_pressed = pygame.key.get_mods() & pygame.KMOD_CTRL

        # Ctrl+Z to undo
        if ctrl_pressed and key == pygame.K_z:
            self._undo()

        # Ctrl+Y to redo
        elif ctrl_pressed and key == pygame.K_y:
            self._redo()

        # ESC to return to menu
        elif key == pygame.K_ESCAPE:
            self._return_to_menu()

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
        Handle mouse click events on board.

        Args:
            pos: Mouse position (x, y)
        """
        # Convert mouse position to cell coordinates
        cell_pos = self._renderer.get_cell_from_pos(pos)

        if cell_pos:
            self._selected_cell = cell_pos

    def _place_number(self, row: int, col: int, number: int) -> None:
        """
        Place a number in the specified cell using Command Pattern.

        Args:
            row: Row index (0-8)
            col: Column index (0-8)
            number: Number to place (1-9)
        """
        # Check if cell is given (cannot modify)
        cell = self._board.get_cell(row, col)
        if cell.is_given:
            print(f"Cannot modify given cell at ({row}, {col})")
            return

        # Create and execute command
        command = SetCellCommand(self._board, row, col, number)
        self._command_history.execute(command)

        # Record move in statistics
        self._statistics.record_move()

        # Check if board is solved
        if self._validator.is_board_solved(self._board):
            print("Congratulations! Puzzle solved!")
            self._timer.stop()  # Stop timer on win
            self._state = config.STATE_WON

    def _clear_cell(self, row: int, col: int) -> None:
        """
        Clear the specified cell using Command Pattern.

        Args:
            row: Row index (0-8)
            col: Column index (0-8)
        """
        # Check if cell is given (cannot modify)
        cell = self._board.get_cell(row, col)
        if cell.is_given:
            print(f"Cannot modify given cell at ({row}, {col})")
            return

        # Create and execute command
        command = ClearCellCommand(self._board, row, col)
        self._command_history.execute(command)

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

    def _undo(self) -> None:
        """
        Undo the last action.

        Uses Command Pattern to reverse the last executed command.
        """
        if self._command_history.undo():
            self._statistics.record_undo()
            print(f"Undo: {self._command_history.get_redo_size()} actions available to redo")
        else:
            print("Nothing to undo")

    def _redo(self) -> None:
        """
        Redo the last undone action.

        Uses Command Pattern to re-execute the last undone command.
        """
        if self._command_history.redo():
            self._statistics.record_redo()
            print(f"Redo: {self._command_history.get_history_size()} total actions")
        else:
            print("Nothing to redo")

    def _use_hint(self) -> None:
        """
        Use the hint system to reveal a cell.

        Gets a hint from HintProvider and places it using Command Pattern.
        """
        if not self._board:
            return

        hint = self._hint_provider.get_hint(self._board)

        if hint:
            row, col, value = hint
            print(f"Hint: Cell ({row}, {col}) should be {value}")

            # Record hint usage
            self._statistics.record_hint()

            # Select the hinted cell
            self._selected_cell = (row, col)

            # Place the number using command (for undo support)
            self._place_number(row, col, value)
        else:
            print("No hints available (puzzle complete or unsolvable)")

    def _update(self) -> None:
        """Update game state."""
        # TODO: Add timer update in Phase 4
        # TODO: Add animation updates in Phase 5
        pass

    def _render(self) -> None:
        """Render the current frame."""
        # Clear screen
        self._screen.fill(config.WHITE)

        if self._state == config.STATE_MENU:
            self._render_menu()
        elif self._state == config.STATE_PLAYING:
            self._render_game()
        elif self._state == config.STATE_WON:
            self._render_game()  # Still show board
            self._render_victory()

        # Update display
        pygame.display.flip()

    def _render_menu(self) -> None:
        """Render main menu."""
        # Title
        font_title = pygame.font.Font(None, config.FONT_SIZE_TITLE)
        title_surface = font_title.render("Sudoku Master", True, config.BLACK)
        title_rect = title_surface.get_rect(center=(config.SCREEN_WIDTH // 2, 80))
        self._screen.blit(title_surface, title_rect)

        # Subtitle
        font_ui = pygame.font.Font(None, config.FONT_SIZE_UI)
        subtitle_surface = font_ui.render("Select Difficulty:", True, config.DARK_GRAY)
        subtitle_rect = subtitle_surface.get_rect(center=(config.SCREEN_WIDTH // 2, 120))
        self._screen.blit(subtitle_surface, subtitle_rect)

        # Difficulty buttons
        self._easy_button.render(self._screen)
        self._medium_button.render(self._screen)
        self._hard_button.render(self._screen)

    def _render_game(self) -> None:
        """Render game board."""
        # Render board
        self._renderer.render_board(self._board, self._selected_cell)

        # Render UI elements with real timer
        timer_text = self._timer.get_formatted_time()
        self._renderer.render_ui(timer_text=timer_text)

        # Render statistics
        self._render_statistics()

        # Render New Game button
        self._new_game_button.render(self._screen)

        # Render Hint button
        self._hint_button.render(self._screen)

    def _render_statistics(self) -> None:
        """Render game statistics."""
        font = pygame.font.Font(None, 20)

        # Position at bottom left
        y_offset = 650
        x_offset = 30

        # Render statistics
        stats_text = [
            f"Moves: {self._statistics.moves}",
            f"Hints: {self._statistics.hints_used}",
            f"Undos: {self._statistics.undos}",
        ]

        for i, text in enumerate(stats_text):
            surface = font.render(text, True, config.DARK_GRAY)
            self._screen.blit(surface, (x_offset, y_offset + i * 20))

    def _render_victory(self) -> None:
        """Render victory message."""
        # Semi-transparent overlay
        overlay = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(config.WHITE)
        self._screen.blit(overlay, (0, 0))

        # Victory text
        font_title = pygame.font.Font(None, config.FONT_SIZE_TITLE)
        victory_surface = font_title.render("Congratulations!", True, config.GREEN)
        victory_rect = victory_surface.get_rect(center=(config.SCREEN_WIDTH // 2, 250))
        self._screen.blit(victory_surface, victory_rect)

        # Time and statistics
        font_ui = pygame.font.Font(None, config.FONT_SIZE_UI)
        time_text = f"Time: {self._timer.get_formatted_time()}"
        time_surface = font_ui.render(time_text, True, config.BLACK)
        time_rect = time_surface.get_rect(center=(config.SCREEN_WIDTH // 2, 290))
        self._screen.blit(time_surface, time_rect)

        moves_text = f"Moves: {self._statistics.moves} | Hints: {self._statistics.hints_used}"
        moves_surface = font_ui.render(moves_text, True, config.BLACK)
        moves_rect = moves_surface.get_rect(center=(config.SCREEN_WIDTH // 2, 320))
        self._screen.blit(moves_surface, moves_rect)

        # Instruction text
        instruction_surface = font_ui.render("Press ESC for menu", True, config.BLACK)
        instruction_rect = instruction_surface.get_rect(center=(config.SCREEN_WIDTH // 2, 360))
        self._screen.blit(instruction_surface, instruction_rect)
