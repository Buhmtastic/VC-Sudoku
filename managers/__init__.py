"""
Managers package for game management classes.
Includes CommandHistory, HintProvider, Timer, SaveManager, and StatisticsManager.
"""

from managers.command_history import CommandHistory
from managers.hint_provider import HintProvider

__all__ = ['CommandHistory', 'HintProvider']
