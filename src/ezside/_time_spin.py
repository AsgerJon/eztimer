"""The TimeSpin widget shows two spin boxes for minutes and seconds."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Optional

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QHBoxLayout, QSpinBox, \
  QAbstractSpinBox
from vistutils import maybeTypes, stringList, searchKey, maybe, maybeType
from vistutils.fields import apply

from utils import parseParentWidget, CustomField

plusMinus = QAbstractSpinBox.ButtonSymbols.PlusMinus


class TimeSpin(QWidget):
  """The TimeSpin widget shows two spin boxes for minutes and seconds."""

  value = CustomField()

  @staticmethod
  def _parseKwargs(**kwargs) -> Optional[int]:
    """Parses keyword arguments"""
    secondsKeys = stringList("""seconds, sec, s, time""")
    secondsKwarg = searchKey(int, *secondsKeys, **kwargs)
    minutesKeys = stringList("""minutes, min, m""")
    minutesKwarg = searchKey(int, *minutesKeys, **kwargs)
    if isinstance(minutesKwarg, int) and isinstance(secondsKwarg, int):
      return minutesKwarg * 60 + secondsKwarg
    if isinstance(minutesKwarg, int):
      return minutesKwarg * 60
    if isinstance(secondsKwarg, int):
      return secondsKwarg

  @staticmethod
  def _parseArgs(*args) -> Optional[int]:
    """Parses positional arguments"""
    return sum([i * j for (i, j) in zip(maybeTypes(int, *args), [60, 1, ])])

  @staticmethod
  def _createSpinbox(value: int) -> QSpinBox:
    """Creates a spinbox"""
    spinBox = QSpinBox()
    spinBox.setRange(0, 59)
    spinBox.setSingleStep(1)
    spinBox.setButtonSymbols(plusMinus)
    spinBox.setValue(value % 60)
    return spinBox

  valueChanged = Signal(int, )

  __time_default__ = 225

  def __init__(self, *args, **kwargs) -> None:
    parent = parseParentWidget(*args, **kwargs)
    QWidget.__init__(self, parent, )
    timeArg = maybeType(int, *args)
    time = maybe(timeArg, self.__time_default__)
    minutes, seconds = 0, 0
    if isinstance(time, int):
      minutes = time // 60
      seconds = time - minutes * 60
    else:
      raise TypeError
    self._minutesSpinBox = self._createSpinbox(minutes)
    self._minutesSpinBox.valueChanged.connect(self._notifyValueChange)
    self._secondsSpinBox = self._createSpinbox(seconds)
    self._secondsSpinBox.valueChanged.connect(self._notifyValueChange)
    self._baseLayout = QHBoxLayout()

  def setupWidgets(self) -> None:
    """Sets up the widgets"""
    self._baseLayout.addWidget(self._minutesSpinBox, )
    self._baseLayout.addWidget(self._secondsSpinBox, )
    self.setLayout(self._baseLayout)

  def show(self) -> None:
    """Reimplementation"""
    self.setupWidgets()
    QWidget.show(self)

  @apply('value', 'get')
  def _getValue(self, ) -> int:
    """Getter-function for the time in seconds currently shown."""
    return self._secondsSpinBox.value() + 60 * self._minutesSpinBox.value()

  @apply('value', 'set')
  def _setValue(self, value: int) -> None:
    """Setter-function for the time in seconds to show."""
    minutes = value // 60
    seconds = value - (minutes * 60)
    self._minutesSpinBox.setValue(minutes)
    self._secondsSpinBox.setValue(seconds)

  def _notifyValueChange(self, *args) -> None:
    """Emits the value change signal"""
    self.valueChanged.emit(self.value)
