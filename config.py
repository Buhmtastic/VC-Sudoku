"""
Game configuration constants for Sudoku Master.
All magic numbers should be defined here following OOP best practices.
"""

# Screen settings
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700
FPS = 60

# Board settings
BOARD_SIZE = 9
BOX_SIZE = 3
CELL_SIZE = 60
BOARD_OFFSET_X = 30
BOARD_OFFSET_Y = 100

# Grid line widths
THIN_LINE_WIDTH = 1
THICK_LINE_WIDTH = 4

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (240, 240, 240)
DARK_GRAY = (100, 100, 100)
LIGHT_BLUE = (200, 220, 255)
DARK_BLUE = (100, 150, 255)
RED = (255, 100, 100)
GREEN = (100, 255, 100)
YELLOW = (255, 255, 150)

# Cell colors
CELL_GIVEN_COLOR = (50, 50, 50)          # Initial numbers (dark gray)
CELL_USER_COLOR = (0, 100, 200)          # User input (blue)
CELL_INVALID_COLOR = (255, 50, 50)       # Invalid (red)
CELL_SELECTED_COLOR = (255, 255, 150)    # Selected (yellow)
CELL_HIGHLIGHT_COLOR = (220, 240, 255)   # Same number highlight (light blue)

# Background colors
BG_COLOR = WHITE
GRID_COLOR = BLACK
BOX_BORDER_COLOR = BLACK

# Difficulty settings
EASY_CELLS_TO_REMOVE = 40      # 41 cells provided
MEDIUM_CELLS_TO_REMOVE = 51    # 30 cells provided
HARD_CELLS_TO_REMOVE = 56      # 25 cells provided

# Font settings
FONT_SIZE_CELL = 40
FONT_SIZE_UI = 24
FONT_SIZE_TITLE = 36
FONT_SIZE_BUTTON = 20

# UI element positions
TITLE_Y = 30
TIMER_X = 450
TIMER_Y = 30
BUTTON_HEIGHT = 40
BUTTON_WIDTH = 120
BUTTON_SPACING = 10

# Command history settings
MAX_HISTORY_SIZE = 100  # Maximum undo/redo history

# Save file paths
SAVE_FILE_PATH = "data/save_game.json"
STATISTICS_FILE_PATH = "data/statistics.json"

# Game states
STATE_MENU = "menu"
STATE_PLAYING = "playing"
STATE_PAUSED = "paused"
STATE_WON = "won"
