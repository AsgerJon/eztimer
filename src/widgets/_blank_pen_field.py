"""The BlankPenField provides an instance insensitive descriptor class
allowing a widget class to access an empty pen. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Never

from PySide6.QtCore import Qt
from PySide6.QtGui import QPen, QColor
from vistutils.fields import AbstractField


class BlankPenField(AbstractField):
  """The BlankPenField provides an instance insensitive descriptor class
  allowing a widget class to access an empty pen. """

  def __prepare_owner__(self, owner: type) -> type:
    """Implementation of abstractmethod. Creates a blank pen at sets it on
    the owner. """
    blankPen = QPen()
    blankPen.setColor(QColor(0, 0, 0, 0, ))
    blankPen.setStyle(Qt.PenStyle.NoPen)
    blankPen.setWidth(1)
    setattr(owner, '__blank_pen__', blankPen)
    return owner

  def __get__(self, _, owner: type) -> QPen:
    """Getter-function implementation is instance insensitive."""
    pen = getattr(owner, '__blank_pen__', )
    if isinstance(pen, QPen):
      return pen
    raise AttributeError

  def __set__(self, *_) -> Never:
    """Illegal setter"""
    raise TypeError

  def __del__(self, *_) -> Never:
    """Illegal setter"""
    raise TypeError
