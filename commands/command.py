"""
Command module for Sudoku Master.
Implements the Command abstract base class for Command Pattern.
"""

from abc import ABC, abstractmethod


class Command(ABC):
    """
    Abstract base class for all commands.

    Responsibility: Define interface for executable and reversible actions

    OOP Principles Applied:
    - Command Pattern: Encapsulates actions as objects
    - Abstraction: Defines interface for all commands
    - Polymorphism: All commands implement same interface
    - Single Responsibility: Each command encapsulates one action

    This pattern enables:
    - Unlimited Undo/Redo functionality
    - Action history tracking
    - Macro commands (future enhancement)
    """

    @abstractmethod
    def execute(self) -> None:
        """
        Execute the command.

        This method performs the action that the command represents.
        Must be implemented by all concrete command classes.
        """
        pass

    @abstractmethod
    def undo(self) -> None:
        """
        Undo the command.

        This method reverses the action performed by execute().
        Must be implemented by all concrete command classes.
        """
        pass

    @abstractmethod
    def get_description(self) -> str:
        """
        Get a human-readable description of the command.

        Returns:
            str: Description of what this command does
        """
        pass
