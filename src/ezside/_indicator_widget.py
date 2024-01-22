"""The IndicatorWidget shows the remaining time on seven segment display
types."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QHBoxLayout, QLCDNumber
from vistutils import maybeType, maybe, stringList, searchKey
from vistutils.fields import apply

from utils import parseParentWidget, CustomField


class IndicatorWidget(QLCDNumber):
  """The IndicatorWidget shows the remaining time on seven segment display
types."""

  value = CustomField()

  def __init__(self, *args, **kwargs) -> None:
    parent = parseParentWidget(*args, **kwargs)
    QLCDNumber.__init__(self, parent)
    self.display('13:37')
    self.setMinimumSize(QSize(128, 64))
    self.setDigitCount(5)
    self._baseLayout = QHBoxLayout()
    self._innerValue = None
    valueKeys = stringList("""value, time""")
    valueKwarg = searchKey(int, *valueKeys, **kwargs)
    valueArg = maybeType(int, *args)
    valueDefault = 225
    value = maybe(valueKwarg, valueArg, valueDefault)

    if isinstance(value, int):
      self.__val0__ = value
    else:
      raise TypeError

  @apply('value', 'get')
  def _getValue(self) -> int:
    """Getter-function for the currently displayed value"""
    return self._innerValue

  @apply('value', 'set')
  def _setValue(self, value: int) -> None:
    """Setter-function for the display value"""
    self._innerValue = value
    minutes = value // 60
    seconds = value - 60 * minutes
    strValue = '%02d:%02d' % (minutes, seconds)
    self.display(strValue)

  def show(self) -> None:
    """Reimplementation"""
    self.value = self.__val0__
    return QLCDNumber.show(self)
