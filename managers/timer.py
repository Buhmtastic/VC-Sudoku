"""
Timer module for Sudoku Master.
Implements game timer functionality.
"""

import time


class Timer:
    """
    Manages game timer.

    Responsibility: Track elapsed game time

    OOP Principles Applied:
    - Single Responsibility: Only manages time tracking
    - Encapsulation: Timer state is private

    Features:
    - Start/stop timer
    - Pause/resume timer
    - Get elapsed time
    - Format time as string

    Attributes:
        _start_time: Time when timer started
        _elapsed_time: Total elapsed time
        _is_running: Whether timer is currently running
        _is_paused: Whether timer is paused
        _pause_start: Time when pause started
    """

    def __init__(self):
        """Initialize Timer with stopped state."""
        self._start_time: float = 0.0
        self._elapsed_time: float = 0.0
        self._is_running: bool = False
        self._is_paused: bool = False
        self._pause_start: float = 0.0

    def start(self) -> None:
        """
        Start the timer.

        Resets elapsed time and begins counting.
        """
        self._start_time = time.time()
        self._elapsed_time = 0.0
        self._is_running = True
        self._is_paused = False
        self._pause_start = 0.0

    def stop(self) -> None:
        """
        Stop the timer.

        Stops counting and resets state.
        """
        self._is_running = False
        self._is_paused = False
        self._elapsed_time = 0.0

    def pause(self) -> None:
        """
        Pause the timer.

        Stops counting but preserves elapsed time.
        Can be resumed later.
        """
        if self._is_running and not self._is_paused:
            self._is_paused = True
            self._pause_start = time.time()

    def resume(self) -> None:
        """
        Resume the timer from pause.

        Continues counting from where it was paused.
        """
        if self._is_running and self._is_paused:
            # Add pause duration to start time (effectively ignoring pause time)
            pause_duration = time.time() - self._pause_start
            self._start_time += pause_duration
            self._is_paused = False
            self._pause_start = 0.0

    def get_elapsed_time(self) -> float:
        """
        Get elapsed time in seconds.

        Returns:
            float: Elapsed time in seconds

        If timer is running and not paused, returns current elapsed time.
        If paused, returns time up to pause.
        If stopped, returns 0.
        """
        if not self._is_running:
            return 0.0

        if self._is_paused:
            # Return time up to when pause started
            return self._pause_start - self._start_time
        else:
            # Return current elapsed time
            return time.time() - self._start_time

    def get_formatted_time(self) -> str:
        """
        Get formatted time string.

        Returns:
            str: Time formatted as MM:SS

        Examples:
            - 65 seconds -> "01:05"
            - 125 seconds -> "02:05"
            - 3661 seconds -> "61:01"
        """
        elapsed = self.get_elapsed_time()
        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        return f"{minutes:02d}:{seconds:02d}"

    @property
    def is_running(self) -> bool:
        """
        Check if timer is running.

        Returns:
            bool: True if timer is running (even if paused)
        """
        return self._is_running

    @property
    def is_paused(self) -> bool:
        """
        Check if timer is paused.

        Returns:
            bool: True if timer is paused
        """
        return self._is_paused
