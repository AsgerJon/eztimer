"""The FillWidget class implements a widget filled with full color. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPaintEvent, QPainter, QBrush, QPen
from PySide6.QtWidgets import QWidget
from vistutils import maybeType, maybe, maybeTypes
from vistutils.fields import TypedField


class FillWidget(QWidget):
  """The FillWidget class implements a widget filled with full color. """

  backgroundColor = TypedField(QColor, QColor(255, 255, 255, 255))
  frameColor = TypedField(QColor, QColor(0, 0, 0, 255))
  frameWidth = TypedField(int, 1)

  def __init__(self, *args, **kwargs) -> None:
    parentKwarg = kwargs.get('parent', None)
    parentArg = maybeType(QWidget, *args)
    parent = maybe(parentKwarg, parentArg)
    if parent is None:
      QWidget.__init__(self, )
    else:
      QWidget.__init__(self, parent)
    self.setMinimumSize(48, 48)
    bgColorKwarg = kwargs.get('backgroundColor', None)
    frameColorKwarg = kwargs.get('frameColor', None)
    colorArgs = [maybeTypes(QColor, *args), None, None]
    bgColorArg, frameColorArg = colorArgs[:2]
    bgColorDefault = QColor(255, 255, 255, 255)
    frameColorDefault = QColor(0, 0, 0, 255)
    bgColor = maybe(bgColorKwarg, bgColorArg, bgColorDefault)
    frameColor = maybe(frameColorKwarg, frameColorArg, frameColorDefault)
    if isinstance(bgColor, QColor):
      self.backgroundColor = bgColor
    else:
      raise TypeError
    if isinstance(frameColor, QColor):
      self.frameColor = frameColor
    else:
      raise TypeError

  def _getPen(self) -> QPen:
    """Getter-function for QPen instance"""
    pen = QPen()
    pen.setColor(self.frameColor)
    pen.setStyle(Qt.PenStyle.SolidLine)
    pen.setWidth(self.frameWidth)
    return pen

  def _getBrush(self) -> QBrush:
    """Getter-function for QBrush instance"""
    brush = QBrush()
    brush.setColor(self.backgroundColor)
    brush.setStyle(Qt.BrushStyle.SolidPattern)
    return brush

  def paintEvent(self, event: QPaintEvent) -> None:
    """Implementation of paint event"""
    p = QPainter()
    p.begin(self)
    viewRect = p.viewport()
    p.setBrush(self._getBrush())
    p.setPen(self._getPen())
    p.drawRect(viewRect)
    p.end()
