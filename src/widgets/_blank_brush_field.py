"""The BlankBrushField provides an instance insensitive descriptor class
allowing a widget class to access an empty brush. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Never

from PySide6.QtCore import Qt
from PySide6.QtGui import QPen, QColor, QBrush
from vistutils.fields import AbstractField


class BlankBrushField(AbstractField):
  """The BlankBrushField provides an instance insensitive descriptor class
  allowing a widget class to access an empty brush. """

  def __prepare_owner__(self, owner: type) -> type:
    """Implementation of abstractmethod. Creates a blank pen at sets it on
    the owner. """
    blankBrush = QBrush()
    blankBrush.setColor(QColor(0, 0, 0, 0, ))
    blankBrush.setStyle(Qt.BrushStyle.NoBrush)
    setattr(owner, '__blank_brush__', blankBrush)
    return owner

  def __get__(self, _, owner: type) -> QBrush:
    """Getter-function implementation is instance insensitive."""
    brush = getattr(owner, '__blank_brush__', )
    if isinstance(brush, QBrush):
      return brush
    raise AttributeError

  def __set__(self, *_) -> Never:
    """Illegal setter"""
    raise TypeError

  def __del__(self, *_) -> Never:
    """Illegal setter"""
    raise TypeError
