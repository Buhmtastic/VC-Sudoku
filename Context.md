# Sudoku Master - Development Context

## Project Overview

**Name**: Sudoku Master (스도쿠 마스터)
**Type**: Puzzle Game (Classic 9x9 Sudoku)
**Platform**: PC (Python + PyGame)
**Development Period**: 5 weeks
**Purpose**: Portfolio project demonstrating OOP mastery and algorithmic skills

---

## Critical Development Principle: Object-Oriented Programming (OOP)

### Importance: CRITICAL - Project will fail if not followed

**ALL code MUST strictly adhere to OOP principles:**

1. **Encapsulation**: All attributes MUST be private (prefixed with `_`). Access through public methods only.
2. **Inheritance**: Common UI components abstracted into parent classes.
3. **Polymorphism**: Difficulty strategies handled through unified interface.
4. **Abstraction**: Puzzle generation/validation algorithms defined via interfaces.

**SOLID Principles - MUST Follow:**
- **S**ingle Responsibility: Each class has ONE responsibility
- **O**pen/Closed: Open for extension, closed for modification
- **L**iskov Substitution: Difficulty strategies are interchangeable
- **I**nterface Segregation: Small, focused interfaces
- **D**ependency Inversion: Depend on abstractions, not concrete implementations

---

## Project Structure

```
sudoku/
├── main.py                     # Game entry point
├── game.py                     # Game class (main game loop)
├── board.py                    # Board class (9x9 grid manager)
├── cell.py                     # Cell class (individual cell state)
├── validator.py                # Validator class (rule checking)
├── solver.py                   # Solver class (backtracking algorithm)
├── puzzle_generator.py         # PuzzleGenerator class
├── strategies/                 # Strategy Pattern for difficulty
│   ├── difficulty_strategy.py  # Abstract Strategy
│   ├── easy_strategy.py
│   ├── medium_strategy.py
│   └── hard_strategy.py
├── commands/                   # Command Pattern for Undo/Redo
│   ├── command.py              # Command abstract class
│   ├── set_cell_command.py
│   └── clear_cell_command.py
├── managers/
│   ├── command_history.py      # CommandHistory class
│   ├── hint_provider.py        # HintProvider class
│   ├── timer.py                # Timer class
│   ├── save_manager.py         # SaveManager class
│   └── statistics_manager.py
├── ui/
│   ├── renderer.py             # UI rendering
│   └── button.py               # Button class
├── config.py                   # Game constants
├── data/                       # Save data
└── tests/                      # Test code
```

---

## Core Classes Design

### 1. Cell Class
**Responsibility**: Manage individual cell state

```python
class Cell:
    """Represents a single cell in the Sudoku board"""

    def __init__(self, value=0, is_given=False):
        self._value = value           # Private: cell value (0-9)
        self._is_given = is_given     # Private: is initial value?
        self._is_valid = True         # Private: validation state

    # Public interface
    def set_value(self, value): pass
    def clear(self): pass
    def mark_invalid(self): pass
    def mark_valid(self): pass

    # Properties (read-only)
    @property
    def value(self): return self._value
    @property
    def is_given(self): return self._is_given
    @property
    def is_valid(self): return self._is_valid
    @property
    def is_empty(self): return self._value == 0
```

**OOP Compliance:**
- All attributes are private
- Access via public methods
- Read-only properties
- Single responsibility: cell state only

---

### 2. Board Class
**Responsibility**: Manage 9x9 grid

```python
class Board:
    """9x9 Sudoku board manager"""

    def __init__(self):
        self._cells = [[Cell() for _ in range(9)] for _ in range(9)]  # Private
        self._validator = None  # Dependency injection

    def set_validator(self, validator):
        """Inject validator (Dependency Injection)"""
        self._validator = validator

    # Public interface
    def get_cell(self, row, col): pass
    def set_cell(self, row, col, value): pass
    def clear_cell(self, row, col): pass
    def is_full(self): pass
    def reset(self): pass
```

**OOP Compliance:**
- _cells is encapsulated (private)
- Access only through get_cell/set_cell
- Validator dependency injection
- Single responsibility: board management

---

### 3. Validator Class
**Responsibility**: Validate Sudoku rules

```python
class Validator:
    """Sudoku rule validation"""

    def is_valid_move(self, board, row, col, num):
        """Check if number placement is valid"""
        return (self._check_row(board, row, num) and
                self._check_column(board, col, num) and
                self._check_box(board, row, col, num))

    def is_board_solved(self, board): pass

    # Private methods (internal implementation)
    def _check_row(self, board, row, num): pass
    def _check_column(self, board, col, num): pass
    def _check_box(self, board, row, col, num): pass
```

**OOP Compliance:**
- Single responsibility: validation only
- Internal logic hidden (private methods)
- Separated validation methods for row/column/box

---

### 4. Solver Class
**Responsibility**: Solve Sudoku puzzle using backtracking

```python
class Solver:
    """Backtracking algorithm for solving Sudoku"""

    def __init__(self, validator):
        self._validator = validator  # Dependency injection

    def solve(self, board):
        """Solve board using backtracking"""
        empty_cell = self._find_empty_cell(board)
        if not empty_cell:
            return True  # Board is complete

        row, col = empty_cell
        for num in range(1, 10):
            if self._validator.is_valid_move(board, row, col, num):
                board.set_cell(row, col, num)
                if self.solve(board):
                    return True
                board.clear_cell(row, col)  # Backtrack
        return False

    # Private
    def _find_empty_cell(self, board): pass
```

**OOP Compliance:**
- Single responsibility: solving only
- Validator dependency injection
- Backtracking encapsulated

---

### 5. DifficultyStrategy (Strategy Pattern)
**Responsibility**: Define difficulty-specific logic

```python
from abc import ABC, abstractmethod

class DifficultyStrategy(ABC):
    """Abstract difficulty strategy"""

    @abstractmethod
    def get_cells_to_remove(self):
        """Return number of cells to remove"""
        pass

class EasyStrategy(DifficultyStrategy):
    def get_cells_to_remove(self): return 40  # 41 cells provided

class MediumStrategy(DifficultyStrategy):
    def get_cells_to_remove(self): return 51  # 30 cells provided

class HardStrategy(DifficultyStrategy):
    def get_cells_to_remove(self): return 56  # 25 cells provided
```

**OOP Compliance:**
- Strategy Pattern applied
- Open/Closed principle: easy to add new difficulties
- Polymorphism: all strategies treated uniformly

---

### 6. PuzzleGenerator Class (Factory Pattern)
**Responsibility**: Generate puzzles

```python
class PuzzleGenerator:
    """Sudoku puzzle generator"""

    def __init__(self, solver):
        self._solver = solver

    def generate(self, difficulty_strategy):
        """Generate puzzle (Factory Method)"""
        board = self._create_full_board()
        cells_to_remove = difficulty_strategy.get_cells_to_remove()
        self._remove_numbers(board, cells_to_remove)
        return board

    # Private
    def _create_full_board(self): pass
    def _remove_numbers(self, board, count): pass
```

**OOP Compliance:**
- Factory Pattern applied
- Strategy Pattern integration
- Generation logic encapsulated

---

### 7. Command Pattern (for Undo/Redo)
**Responsibility**: Encapsulate actions as objects

```python
from abc import ABC, abstractmethod

class Command(ABC):
    """Abstract command"""

    @abstractmethod
    def execute(self): pass

    @abstractmethod
    def undo(self): pass

class SetCellCommand(Command):
    """Set cell value command"""

    def __init__(self, board, row, col, new_value):
        self._board = board
        self._row = row
        self._col = col
        self._new_value = new_value
        self._old_value = board.get_cell(row, col).value

    def execute(self):
        self._board.set_cell(self._row, self._col, self._new_value)

    def undo(self):
        self._board.set_cell(self._row, self._col, self._old_value)

class CommandHistory:
    """Manage command history"""

    def __init__(self):
        self._history = []
        self._redo_stack = []

    def execute(self, command): pass
    def undo(self): pass
    def redo(self): pass
```

**OOP Compliance:**
- Command Pattern applied
- History management encapsulated
- Polymorphism: various commands handled uniformly

---

## Development Phases

### Phase 1: Basic Board & UI (Week 1)
- Cell class implementation
- Board class implementation
- Basic game loop
- 9x9 grid rendering
- Mouse/keyboard input

**OOP Checklist:**
- Cell._value is private, accessed via set_value()
- Board._cells is private, accessed via get_cell()
- Single responsibility for each class
- Clear public/private method separation

---

### Phase 2: Validation System (Week 2)
- Validator class implementation
- Board integration with Validator
- Invalid input highlighting
- Game completion detection

**OOP Checklist:**
- Validator has single responsibility
- Validation logic in private methods
- Dependency injection in Board
- Interface segregation

---

### Phase 3: Puzzle Generation (Week 3)
- Solver class (backtracking algorithm)
- PuzzleGenerator class
- DifficultyStrategy abstract class
- Easy/Medium/Hard strategy implementations
- Difficulty selection UI

**OOP Checklist:**
- Strategy Pattern properly implemented
- Factory Pattern for generation
- Open/Closed principle maintained
- Backtracking algorithm encapsulated
- Polymorphism for strategies

---

### Phase 4: Advanced Features (Week 4)
- Command Pattern implementation
- Undo/Redo functionality
- HintProvider class
- Timer class
- SaveManager class

**OOP Checklist:**
- Command Pattern properly applied
- Single responsibility for each manager
- Command history encapsulated
- Polymorphism for various commands
- Dependency injection for HintProvider

---

### Phase 5: Polishing & Deployment (Week 5)
- UI/UX improvements
- StatisticsManager class
- Settings menu
- **OOP code quality final check**
- Bug fixes and testing
- Documentation

**OOP Final Checklist:**
- All classes follow single responsibility
- Proper private/public access control
- Strategy Pattern working correctly
- Command Pattern working correctly
- Sufficient encapsulation
- Docstrings for all classes/methods
- No magic numbers
- No duplicate code

---

## Core Algorithms

### Backtracking Algorithm (Solver)

```
1. Find empty cell
2. If no empty cell, board is solved
3. For each number 1-9:
   a. If number is valid at position
   b. Place number
   c. Recursively solve
   d. If solution found, return success
   e. Otherwise, remove number (backtrack)
4. Return failure if all numbers tried
```

**Time Complexity**: O(9^empty_cells) worst case

---

### Puzzle Generation Algorithm

```
1. Create full board:
   - Start with empty board
   - Randomly place some numbers
   - Use backtracking to complete

2. Remove numbers:
   - Remove N cells based on difficulty
   - After each removal, verify unique solution exists
   - If not unique, restore and try next cell

3. Mark remaining cells as "given"
```

---

## Coding Guidelines

### Naming Conventions
- **Classes**: PascalCase (e.g., `Board`, `DifficultyStrategy`)
- **Methods/Functions**: snake_case (e.g., `set_value`, `is_valid_move`)
- **Private attributes**: prefix with `_` (e.g., `_value`, `_cells`)
- **Constants**: UPPER_SNAKE_CASE (e.g., `BOARD_SIZE`, `CELL_SIZE`)

### Access Control
- **Private**: `_attribute`, `_method()` - internal use only
- **Public**: `attribute`, `method()` - external interface
- **Property**: `@property` decorator for read-only access

### Documentation
- Every class MUST have a docstring explaining its responsibility
- Every public method MUST have a docstring
- Complex algorithms MUST have inline comments

### Code Quality Rules
- No magic numbers - all constants in `config.py`
- No duplicate code - extract to methods
- Methods should be <20 lines when possible
- Each class has ONE clear responsibility
- Use type hints for function parameters/returns

---

## Constants (config.py)

```python
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

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_BLUE = (200, 220, 255)
DARK_BLUE = (100, 150, 255)
RED = (255, 100, 100)
GREEN = (100, 255, 100)

# Cell colors
CELL_GIVEN_COLOR = (50, 50, 50)        # Initial numbers (dark gray)
CELL_USER_COLOR = (0, 100, 200)        # User input (blue)
CELL_INVALID_COLOR = (255, 50, 50)     # Invalid (red)
CELL_SELECTED_COLOR = (255, 255, 150)  # Selected (yellow)

# Difficulty
EASY_CELLS_TO_REMOVE = 40
MEDIUM_CELLS_TO_REMOVE = 51
HARD_CELLS_TO_REMOVE = 56

# Fonts
FONT_SIZE_CELL = 40
FONT_SIZE_UI = 24
```

---

## Testing Checklist

### Functional Tests
- [ ] Board renders correctly
- [ ] Cell selection works
- [ ] Number input works
- [ ] Invalid input shows in red
- [ ] Victory condition detected
- [ ] Undo/Redo works
- [ ] Hint button works
- [ ] Timer works
- [ ] Save/Load works
- [ ] Difficulty selection works

### OOP Design Tests (CRITICAL)
- [ ] Class independence: each class testable independently
- [ ] Encapsulation: private attributes not directly accessible
- [ ] Strategy Pattern: difficulty strategies interchangeable
- [ ] Command Pattern: Undo/Redo working
- [ ] Dependency Injection: Board accepts Validator injection
- [ ] Single Responsibility: modifying one class has minimal impact

### Algorithm Tests
- [ ] Backtracking always finds solution
- [ ] Generated puzzles have unique solutions
- [ ] Validation is accurate
- [ ] Difficulty levels are appropriate

### Code Quality Tests
- [ ] Docstrings: all classes and methods documented
- [ ] Naming conventions: consistent PascalCase/snake_case
- [ ] Magic numbers: all defined in config.py
- [ ] Duplicate code: none
- [ ] Method length: mostly <20 lines

---

## Design Pattern Summary

### Strategy Pattern
- **Where**: Difficulty strategies (Easy/Medium/Hard)
- **Why**: Easy to add new difficulty levels without modifying existing code
- **Classes**: `DifficultyStrategy` (abstract), `EasyStrategy`, `MediumStrategy`, `HardStrategy`

### Command Pattern
- **Where**: User actions (SetCell, ClearCell)
- **Why**: Enables unlimited Undo/Redo functionality
- **Classes**: `Command` (abstract), `SetCellCommand`, `ClearCellCommand`, `CommandHistory`

### Factory Method Pattern
- **Where**: Puzzle generation
- **Why**: Creates puzzles based on difficulty strategy
- **Class**: `PuzzleGenerator.generate(difficulty_strategy)`

### Dependency Injection
- **Where**: Board receives Validator, Solver receives Validator, HintProvider receives Solver
- **Why**: Loose coupling, easy testing, flexible composition

---

## Interview Preparation

### Q: "What design patterns did you use?"

**A**: "I applied three main design patterns:

1. **Strategy Pattern**: Difficulty levels are implemented as interchangeable strategies (Easy/Medium/Hard). Adding a new difficulty requires only adding a new strategy class without modifying existing code.

2. **Command Pattern**: All user actions are encapsulated as Command objects, enabling unlimited Undo/Redo. Commands include SetCellCommand and ClearCellCommand, managed by CommandHistory.

3. **Factory Method**: PuzzleGenerator.generate() creates appropriate puzzles based on the difficulty strategy provided.

Additionally, I strictly followed SOLID principles, particularly Single Responsibility - Validator handles validation only, Solver handles solving only, and Generator handles generation only."

---

### Q: "How did you optimize the backtracking algorithm?"

**A**: "I applied three optimizations:

1. **Constraint Propagation**: Pre-calculate possible numbers for each cell to reduce trials.

2. **MRV (Minimum Remaining Values) Heuristic**: Fill cells with fewest possibilities first to trigger early failure.

3. **Early Termination**: When checking for unique solutions, stop immediately after finding 2 solutions.

These optimizations reduced average puzzle generation time to under 0.5 seconds."

---

## Git Workflow

```
main (stable)
  └── develop (development branch)
        ├── feature/phase1-board
        ├── feature/phase2-validation
        ├── feature/phase3-generator
        ├── feature/phase4-commands
        └── feature/phase5-polish
```

**Branch Naming**: `feature/<phase-description>`
**Commit Messages**: Clear, descriptive, present tense (e.g., "Add Cell class with encapsulation")

---

## Technologies

- **Language**: Python 3.8+
- **Game Library**: PyGame 2.5+
- **Version Control**: Git + GitHub
- **Code Quality**: pylint, black
- **Testing**: pytest (optional)

---

## Success Criteria

The project is considered successful when:

1. All 5 phases are completed
2. All OOP checklists pass 100%
3. All design patterns correctly implemented
4. No OOP principle violations
5. Game is stable and bug-free
6. Code is clean and well-documented
7. Ready for portfolio presentation

---

## Anti-Patterns to Avoid

### Do NOT:
- Access `_private` attributes directly from outside the class
- Create god classes that do everything
- Use magic numbers (hard-coded values)
- Duplicate code across methods
- Write methods longer than 30 lines (except necessary cases)
- Skip docstrings
- Violate single responsibility principle
- Use global variables
- Directly modify `Board._cells` from outside Board class

### DO:
- Use public methods to access private data
- Keep classes focused on single responsibility
- Define all constants in config.py
- Extract common logic to reusable methods
- Keep methods short and focused
- Document all public interfaces
- Follow SOLID principles
- Pass dependencies via constructor (dependency injection)
- Use encapsulation properly

---

## Quick Reference

### Key Files by Phase

**Phase 1**: `cell.py`, `board.py`, `game.py`, `config.py`
**Phase 2**: `validator.py`
**Phase 3**: `solver.py`, `puzzle_generator.py`, `strategies/`
**Phase 4**: `commands/`, `managers/`
**Phase 5**: `ui/`, `statistics_manager.py`

### Must-Have Features

- 9x9 Sudoku grid
- Difficulty selection (Easy/Medium/Hard)
- Input validation with visual feedback
- Undo/Redo (unlimited)
- Hint system
- Timer
- Auto-save/load

### OOP Principles Priority

1. **Encapsulation** (HIGHEST priority)
2. **Single Responsibility**
3. **Dependency Injection**
4. **Strategy Pattern**
5. **Command Pattern**

---

This context document should be referenced throughout development to ensure OOP compliance and maintain code quality.
