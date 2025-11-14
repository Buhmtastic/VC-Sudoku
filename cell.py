"""
Cell module for Sudoku Master.
Implements the Cell class following OOP principles.
"""


class Cell:
    """
    Represents a single cell in the Sudoku board.

    Responsibility: Manage individual cell state
    - Store cell value (0-9, where 0 means empty)
    - Track if cell is an initial given value
    - Track validation state

    OOP Principles Applied:
    - Encapsulation: All attributes are private
    - Single Responsibility: Only manages cell state
    - Property Pattern: Read-only access via properties
    """

    def __init__(self, value: int = 0, is_given: bool = False):
        """
        Initialize a cell.

        Args:
            value: Cell value (0-9, where 0 means empty)
            is_given: True if this is an initial puzzle value
        """
        self._value = value           # Private: cell value
        self._is_given = is_given     # Private: is initial value?
        self._is_valid = True         # Private: validation state

    # Public interface methods

    def set_value(self, value: int) -> None:
        """
        Set the cell value.

        Args:
            value: New value (0-9)

        Note: Cannot modify given cells
        """
        if not self._is_given:
            self._value = value

    def clear(self) -> None:
        """Clear the cell value (set to 0)."""
        if not self._is_given:
            self._value = 0

    def mark_invalid(self) -> None:
        """Mark this cell as invalid (rule violation)."""
        self._is_valid = False

    def mark_valid(self) -> None:
        """Mark this cell as valid."""
        self._is_valid = True

    # Properties (read-only access)

    @property
    def value(self) -> int:
        """Get the cell value."""
        return self._value

    @property
    def is_given(self) -> bool:
        """Check if this is an initial given value."""
        return self._is_given

    @property
    def is_valid(self) -> bool:
        """Check if the cell is valid."""
        return self._is_valid

    @property
    def is_empty(self) -> bool:
        """Check if the cell is empty."""
        return self._value == 0

    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"Cell(value={self._value}, given={self._is_given}, valid={self._is_valid})"
