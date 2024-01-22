"""The DialogButtonsWidget provides a widget combining Cancel and Accept
buttons."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton

from utils import parseParentWidget


class DialogButtons(QWidget):
  """The DialogButtonsWidget provides a widget combining Cancel and Accept
  buttons."""

  acceptClick = Signal()
  cancelClick = Signal()

  def __init__(self, *args, **kwargs) -> None:
    parent = parseParentWidget(*args, **kwargs)
    QWidget.__init__(self, parent)
    self._baseLayout = QHBoxLayout()
    self._acceptButton = QPushButton('Accept')
    self._cancelButton = QPushButton('Cancel')
    self._acceptButton.clicked.connect(self._acceptFunc)
    self._cancelButton.clicked.connect(self._cancelFunc)

  def _acceptFunc(self) -> None:
    """Emits accept signal"""
    self.acceptClick.emit()

  def _cancelFunc(self) -> None:
    """Emits cancel signal"""
    self.cancelClick.emit()
