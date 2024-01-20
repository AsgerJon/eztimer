"""The BaseWindow provides the main application window."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtWidgets import QMainWindow, QWidget


class BaseWindow(QMainWindow):
  """The BaseWindow provides the main application window."""

  def __init__(self, *args, **kwargs) -> None:
    parentKwarg = kwargs.get('parent', None)
    parentArg = [*[arg for arg in args if isinstance(arg, QWidget)], None][0]
    QMainWindow.__init__(self, )
