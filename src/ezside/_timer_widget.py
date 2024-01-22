"""TimerWidget provides a widget with time tools and indicators"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Optional

from PySide6.QtCore import QSize, Signal
from PySide6.QtWidgets import (QWidget, QGridLayout, QPushButton,
                               QHBoxLayout)

from ezside import IndicatorWidget, TimerControlWidget
from mediatools import AbstractAudio
from utils import CustomField, parseParentWidget


class TimerWidget(AbstractAudio):
  """TimerWidget provides a widget with time tools and indicators"""

  timeLeft = CustomField()
  timerStart = Signal()
  timerStop = Signal()

  @staticmethod
  def _parseKwargs(**kwargs) -> Optional[QWidget]:
    """Parses keyword arguments"""
    parentKwarg = kwargs.get('parent', None)
    if isinstance(parentKwarg, QWidget):
      return parentKwarg

  @staticmethod
  def _parseArgs(*args) -> Optional[QWidget]:
    """Parses positional arguments"""
    for arg in args:
      if isinstance(arg, QWidget):
        return arg

  def __init__(self, *args, **kwargs) -> None:
    parent = parseParentWidget(*args, **kwargs)
    AbstractAudio.__init__(self, parent)
    self.setMinimumSize(QSize(96, 96))
    self._baseLayout = QHBoxLayout()
    self._indicatorWidget = IndicatorWidget(self)
    self._controlWidget = TimerControlWidget(self)
    self._controlWidget.stopSignal.connect(self.stopSound)

  def updateTime(self, remainingTime: int) -> None:
    """Receives an update for the time"""
    if not remainingTime:
      return self.playSound()
    if remainingTime - self._indicatorWidget.value:
      self._indicatorWidget.value = remainingTime

  def setupWidgets(self) -> None:
    """Sets up the widgets"""
    self._baseLayout.addWidget(self._indicatorWidget)
    self._baseLayout.addWidget(self._controlWidget)
    self.setLayout(self._baseLayout)

  def show(self) -> None:
    """Reimplementation"""
    AbstractAudio.show(self)
