"""The BaseWindow provides the main application window."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow, QWidget, QGridLayout, QPushButton
from vistutils import maybe

from widgets import SevenSegmentWidget
from windows import BaseWindow


class LayoutWindow(BaseWindow):
  """The BaseWindow provides the main application window."""

  def __init__(self, *args, **kwargs) -> None:
    parentKwarg = kwargs.get('parent', None)
    parentArg = [*[arg for arg in args if isinstance(arg, QWidget)], None][0]
    parent = maybe(parentKwarg, parentArg)
    if parent is None:
      QMainWindow.__init__(self, )
    else:
      QMainWindow.__init__(self, parent)
    self.setMinimumSize(QSize(128, 128))
    self._baseWidget = QWidget()
    self._baseLayout = QGridLayout()
    self._timerWidget = SevenSegmentWidget(self, )
    self._startButton = QPushButton(self)
    self._startButton.setText('START')
    self._cancelButton = QPushButton(self)
    self._cancelButton.setText('CANCEL')
    self._timeButton = QPushButton(self)
    self._timeButton.setText('Set Time')
    self._soundButton = QPushButton(self)
    self._soundButton.setText('Set Sound')

  def setupWidgets(self) -> None:
    """Sets up the widgets | row col"""
    self._baseLayout.addWidget(self._timerWidget, 0, 0, 2, 2)
    self._baseLayout.addWidget(self._startButton, 2, 0, 1, 1, )
    self._baseLayout.addWidget(self._cancelButton, 2, 1, 1, 1, )
    self._baseLayout.addWidget(QWidget(), 2, 2, 1, 1)
    self._baseLayout.addWidget(self._timeButton, 1, 2, 1, 1)
    self._baseLayout.addWidget(self._soundButton, 0, 2, 1, 1)
    self._baseWidget.setLayout(self._baseLayout)
    self.setCentralWidget(self._baseWidget)
