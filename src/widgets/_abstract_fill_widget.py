"""The FillWidget class implements a minimum size and paints a solid color
on the paint event."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from abc import abstractmethod

from PySide6.QtGui import QPaintEvent, QPainter
from PySide6.QtWidgets import QWidget

from utils import CustomField
from widgets import AbstractAudio, BlankPenField, BlankBrushField


class AbstractFillWidget(AbstractAudio):
  """The FillWidget class implements a minimum size and paints a solid color
  on the paint event."""

  backgroundBrush = CustomField()
  backgroundPen = CustomField()
  blankPen = BlankPenField()
  blankBrush = BlankBrushField()

  def __init__(self, *args, **kwargs) -> None:
    QWidget.__init__(self, *args, **kwargs)

  @abstractmethod
  def initializePlayer(self) -> None:
    """Subclasses must implement this method. It is invoked as part of the
    show method, and the media player must have a source after this
    method is invoked."""

  def paintEvent(self, paintEvent: QPaintEvent) -> None:
    """Implementation of painting."""
    p = QPainter()
    p.begin(self)
    viewRect = p.viewport()
    p.end()
