"""
CommandHistory module for Sudoku Master.
Implements command history management for Undo/Redo functionality.
"""

from typing import List
from commands.command import Command


class CommandHistory:
    """
    Manages command history for Undo/Redo functionality.

    Responsibility: Track executed commands and support undo/redo operations

    OOP Principles Applied:
    - Single Responsibility: Only manages command history
    - Encapsulation: History and redo stack are private
    - Command Pattern Integration: Works with Command interface

    This class enables:
    - Unlimited undo
    - Unlimited redo
    - Clear history
    - Check if undo/redo is possible

    Attributes:
        _history: Stack of executed commands
        _redo_stack: Stack of undone commands (for redo)
    """

    def __init__(self):
        """Initialize CommandHistory with empty history and redo stack."""
        self._history: List[Command] = []
        self._redo_stack: List[Command] = []

    def execute(self, command: Command) -> None:
        """
        Execute a command and add it to history.

        Args:
            command: The command to execute

        This method:
        1. Executes the command
        2. Adds it to history
        3. Clears the redo stack (new action invalidates redo)
        """
        command.execute()
        self._history.append(command)
        self._redo_stack.clear()  # New action clears redo stack

    def undo(self) -> bool:
        """
        Undo the last command.

        Returns:
            bool: True if undo was successful, False if nothing to undo

        This method:
        1. Pops the last command from history
        2. Calls its undo() method
        3. Pushes it to the redo stack
        """
        if not self.can_undo():
            return False

        command = self._history.pop()
        command.undo()
        self._redo_stack.append(command)
        return True

    def redo(self) -> bool:
        """
        Redo the last undone command.

        Returns:
            bool: True if redo was successful, False if nothing to redo

        This method:
        1. Pops the last command from redo stack
        2. Calls its execute() method
        3. Pushes it back to history
        """
        if not self.can_redo():
            return False

        command = self._redo_stack.pop()
        command.execute()
        self._history.append(command)
        return True

    def can_undo(self) -> bool:
        """
        Check if undo is possible.

        Returns:
            bool: True if there are commands in history to undo
        """
        return len(self._history) > 0

    def can_redo(self) -> bool:
        """
        Check if redo is possible.

        Returns:
            bool: True if there are commands in redo stack
        """
        return len(self._redo_stack) > 0

    def clear(self) -> None:
        """
        Clear all command history.

        This removes all commands from both history and redo stack.
        Useful when starting a new game.
        """
        self._history.clear()
        self._redo_stack.clear()

    def get_history_size(self) -> int:
        """
        Get the number of commands in history.

        Returns:
            int: Number of commands that can be undone
        """
        return len(self._history)

    def get_redo_size(self) -> int:
        """
        Get the number of commands in redo stack.

        Returns:
            int: Number of commands that can be redone
        """
        return len(self._redo_stack)

    def get_last_command_description(self) -> str:
        """
        Get description of the last command in history.

        Returns:
            str: Description of last command, or empty string if no history
        """
        if self.can_undo():
            return self._history[-1].get_description()
        return ""
