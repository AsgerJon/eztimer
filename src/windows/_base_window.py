"""BaseWindow subclasses QMainWindow defining the base layer of the
main application window. This class is responsible for defining the
menu bar, the status bar and actions."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from abc import abstractmethod

from PySide6.QtWidgets import QMainWindow
from vistutils.fields import apply

from utils import parseParentWidget


class BaseWindow(QMainWindow):
  """BaseWindow subclasses QMainWindow defining the base layer of the
  main application window. """

  def __init__(self, *args, **kwargs) -> None:
    parent = parseParentWidget(*args, **kwargs)
    QMainWindow.__init__(self, parent)

  def show(self, ) -> None:
    """Ensures that setupWidgets runs before the parent show method"""
    self.setupWidgets()
    QMainWindow.show(self)

  @abstractmethod
  def setupWidgets(self, ) -> None:
    """Method responsible for setting up the widgets. Subclasses must
    implement this method."""

