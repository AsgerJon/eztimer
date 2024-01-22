"""The MenuBar provides a subclass of QMenuBar used by BaseWindow"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenuBar, QWidget, QMainWindow

from utils import parseParentWidget


def actionFactory(name: str, parent: QMainWindow) -> QAction:
  """Factory function for QAction"""


class MenuBar(QMenuBar):
  """The MenuBar provides a subclass of QMenuBar used by BaseWindow"""

  def __init__(self, *args, **kwargs) -> None:
    parent = parseParentWidget(*args, **kwargs)
    if parent is None:
      e = """Failed to parse parent of type '%s'!"""
      raise TypeError(e % QWidget)
    QMenuBar.__init__(self, parent)
