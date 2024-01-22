"""The 'actionFactory' function creates named actions for a given parent. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow

from windows import BaseWindow


def actionFactory(name: str, baseWindow: BaseWindow) -> QAction:
  """The 'actionFactory' function creates named actions for a given
  parent. """

