"""The TimerControlWidget provides a widget with buttons providing
controls."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Signal, QSize
from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout

from ezside import TimeDialog, TimeSpin
from utils import parseParentWidget


class TimerControlWidget(QWidget):
  """The TimerControlWidget provides a widget with buttons providing
  controls."""

  startSignal = Signal()
  stopSignal = Signal()
  pauseSignal = Signal()
  resumeSignal = Signal()
  timeSignal = Signal(int)
  timeChanged = Signal(int)

  def __init__(self, *args, **kwargs) -> None:
    parent = parseParentWidget(*args, **kwargs)
    QWidget.__init__(self, parent, )
    self.setMinimumSize(QSize(128, 128))
    self._timeDialog = TimeDialog()
    self._timeDialog.acceptSignal.connect(self._acceptTimeFunc)
    self._baseLayout = QGridLayout()
    self._startButton = QPushButton(self)
    self._startButton.setText('START')
    self._startButton.clicked.connect(self.startSignal.emit)
    self._stopButton = QPushButton(self)
    self._stopButton.setText('STOP')
    self._stopButton.clicked.connect(self.stopSignal.emit)
    self._setSound = QPushButton(self)
    self._setSound.setText('Set Sound')
    self._setTime = QPushButton(self)
    self._setTime.setText('Set Time')
    self._setTime.clicked.connect(self._showTimeDialog)
    self._timeValue = TimeSpin.__time_default__

  def _showTimeDialog(self, ) -> None:
    """Opens the time dialog"""
    self._timeDialog.show()

  def _acceptTimeFunc(self, timeValue: int) -> None:
    """Function emitting time signal on accept of time dialog."""
    if timeValue - self._timeValue:
      self._timeValue = timeValue
      self.timeChanged.emit(timeValue)

  def setupWidgets(self, ) -> None:
    """Sets up the widgets"""
    self._baseLayout.addWidget(self._setTime, 0, 0, 1, 2)
    self._baseLayout.addWidget(self._startButton, 1, 0, 1, 1)
    self._baseLayout.addWidget(self._stopButton, 1, 1, 1, 1)
    self._baseLayout.addWidget(self._setSound, 3, 0, 1, 2)
    self.setLayout(self._baseLayout)

  def show(self) -> None:
    """Reimplementation"""
    self.setupWidgets()
    QWidget.show(self)
