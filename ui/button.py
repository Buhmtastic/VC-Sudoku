"""
Button module for Sudoku Master.
Implements the Button class for UI interactions.
"""

import pygame
from typing import Tuple, Optional, Callable
import config


class Button:
    """
    Represents a clickable button.

    Responsibility: Handle button rendering and click detection
    - Draw button with text
    - Detect mouse clicks
    - Execute callback on click
    - Visual feedback (hover, pressed)

    OOP Principles Applied:
    - Single Responsibility: Only handles button behavior
    - Encapsulation: Internal state private
    - Callback Pattern: Flexible action execution
    """

    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        text: str,
        callback: Optional[Callable] = None,
        font_size: int = config.FONT_SIZE_BUTTON
    ):
        """
        Initialize button.

        Args:
            x: X position (top-left)
            y: Y position (top-left)
            width: Button width
            height: Button height
            text: Button text
            callback: Function to call on click
            font_size: Font size for text
        """
        self._rect = pygame.Rect(x, y, width, height)
        self._text = text
        self._callback = callback
        self._font = pygame.font.Font(None, font_size)

        # State
        self._is_hovered = False
        self._is_pressed = False

        # Colors
        self._normal_color = config.LIGHT_GRAY
        self._hover_color = config.LIGHT_BLUE
        self._pressed_color = config.DARK_BLUE
        self._text_color = config.BLACK

    def render(self, screen: pygame.Surface) -> None:
        """
        Render the button.

        Args:
            screen: PyGame surface to draw on
        """
        # Determine color based on state
        if self._is_pressed:
            color = self._pressed_color
        elif self._is_hovered:
            color = self._hover_color
        else:
            color = self._normal_color

        # Draw button background
        pygame.draw.rect(screen, color, self._rect)

        # Draw border
        pygame.draw.rect(screen, config.BLACK, self._rect, 2)

        # Draw text
        text_surface = self._font.render(self._text, True, self._text_color)
        text_rect = text_surface.get_rect(center=self._rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event: pygame.event.Event) -> bool:
        """
        Handle mouse events.

        Args:
            event: PyGame event

        Returns:
            True if button was clicked, False otherwise
        """
        if event.type == pygame.MOUSEMOTION:
            self._is_hovered = self._rect.collidepoint(event.pos)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self._rect.collidepoint(event.pos):
                self._is_pressed = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if self._is_pressed and self._rect.collidepoint(event.pos):
                self._is_pressed = False
                if self._callback:
                    self._callback()
                return True
            self._is_pressed = False

        return False

    def set_text(self, text: str) -> None:
        """
        Update button text.

        Args:
            text: New button text
        """
        self._text = text

    def set_callback(self, callback: Callable) -> None:
        """
        Set button callback function.

        Args:
            callback: Function to call on click
        """
        self._callback = callback

    @property
    def rect(self) -> pygame.Rect:
        """Get button rectangle."""
        return self._rect

    @property
    def text(self) -> str:
        """Get button text."""
        return self._text
