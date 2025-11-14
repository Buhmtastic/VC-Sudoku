# 🧩 Sudoku Master

> A professionally crafted Sudoku game demonstrating OOP principles and advanced algorithms

## 🎯 Highlights

- ✅ **Backtracking Algorithm** for puzzle generation and solving
- ✅ **Strategy Pattern** for difficulty levels (Easy/Medium/Hard)
- ✅ **Command Pattern** for unlimited Undo/Redo
- ✅ **100% OOP Compliance** with SOLID principles
- ✅ **Clean Architecture** with clear separation of concerns

## 🎮 Features

### Core Gameplay
- Classic 9x9 Sudoku puzzle
- Three difficulty levels: Easy, Medium, Hard
- Real-time input validation
- Visual feedback for invalid moves
- Auto-save and load functionality

### Advanced Features
- **Unlimited Undo/Redo**: Command Pattern implementation
- **Hint System**: Get help when stuck
- **Timer**: Track your solving time
- **Statistics**: View your game history and performance

## 🏗️ Architecture

### Key Classes
- **Cell**: Manages individual cell state with encapsulation
- **Board**: Manages 9x9 grid with proper encapsulation
- **Validator**: Rule validation with single responsibility
- **Solver**: Backtracking algorithm implementation
- **PuzzleGenerator**: Factory method for puzzle creation
- **CommandHistory**: Command pattern for Undo/Redo

### Design Patterns
- **Strategy Pattern**: Difficulty levels (Easy/Medium/Hard)
- **Command Pattern**: User actions as objects (Undo/Redo)
- **Factory Method Pattern**: Puzzle generation
- **Dependency Injection**: Loose coupling between components

### SOLID Principles
- **S**ingle Responsibility: Each class has one clear responsibility
- **O**pen/Closed: Open for extension, closed for modification
- **L**iskov Substitution: Difficulty strategies are interchangeable
- **I**nterface Segregation: Small, focused interfaces
- **D**ependency Inversion: Depend on abstractions, not implementations

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/VC-Sudoku.git
cd VC-Sudoku
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the game:
```bash
python main.py
```

## 🎮 How to Play

### Controls
- **Mouse**: Click to select a cell
- **Number Keys (1-9)**: Enter a number
- **Delete/Backspace**: Clear a cell
- **ESC**: Exit game
- **Ctrl+Z**: Undo
- **Ctrl+Y**: Redo

### Rules
1. Each row must contain numbers 1-9 without repetition
2. Each column must contain numbers 1-9 without repetition
3. Each 3x3 box must contain numbers 1-9 without repetition

## 🧠 Algorithms

### Backtracking (Solver)
- Recursive exploration of valid placements
- Early termination on conflicts
- Time complexity: O(9^empty_cells)

**Algorithm Steps:**
1. Find empty cell
2. Try numbers 1-9
3. Check if valid using Validator
4. Recursively solve remaining cells
5. Backtrack if no solution found

### Puzzle Generation
1. **Create complete board**:
   - Start with empty board
   - Randomly place some numbers
   - Use backtracking to complete

2. **Remove numbers**:
   - Remove cells based on difficulty
   - Verify unique solution exists
   - Mark remaining cells as "given"

## 📁 Project Structure

```
sudoku/
├── main.py                     # Game entry point
├── game.py                     # Game class (main loop)
├── board.py                    # Board class
├── cell.py                     # Cell class
├── validator.py                # Validator class
├── solver.py                   # Solver class (backtracking)
├── puzzle_generator.py         # PuzzleGenerator class
├── strategies/                 # Strategy Pattern
│   ├── difficulty_strategy.py
│   ├── easy_strategy.py
│   ├── medium_strategy.py
│   └── hard_strategy.py
├── commands/                   # Command Pattern
│   ├── command.py
│   ├── set_cell_command.py
│   └── clear_cell_command.py
├── managers/                   # Game managers
│   ├── command_history.py
│   ├── hint_provider.py
│   ├── timer.py
│   ├── save_manager.py
│   └── statistics_manager.py
├── ui/                         # UI components
│   ├── renderer.py
│   └── button.py
├── config.py                   # Game constants
├── data/                       # Save data
└── tests/                      # Unit tests
```

## 🧪 Testing

Run tests with pytest:
```bash
pytest tests/
```

## 📊 Development Phases

- ✅ **Phase 1**: Basic Board & UI (Week 1)
- ✅ **Phase 2**: Validation System (Week 2)
- ✅ **Phase 3**: Puzzle Generation (Week 3)
- ✅ **Phase 4**: Advanced Features (Week 4)
- ✅ **Phase 5**: Polishing & Deployment (Week 5)

## 🎓 Learning Outcomes

This project demonstrates:
- **OOP Mastery**: Encapsulation, inheritance, polymorphism, abstraction
- **Design Patterns**: Strategy, Command, Factory Method
- **SOLID Principles**: All five principles applied
- **Algorithm Skills**: Backtracking, constraint satisfaction
- **Software Architecture**: Clean, maintainable code structure

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Portfolio: [yourportfolio.com](https://yourportfolio.com)

## 🙏 Acknowledgments

- Classic Sudoku puzzle game
- Inspired by backtracking algorithms and OOP design principles
- Built as a portfolio project demonstrating professional software development practices

## 📚 Documentation

For detailed development context and guidelines, see:
- [Context.md](Context.md) - Development context and OOP guidelines
- [개발기획서_Sudoku.md](개발기획서_Sudoku.md) - Project planning document (Korean)

---

**Note**: This project prioritizes code quality and OOP principles over feature quantity. Every class follows SOLID principles and demonstrates professional software engineering practices.
