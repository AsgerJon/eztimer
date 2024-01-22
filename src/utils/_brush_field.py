"""BrushField is a descriptor class for QBrush typed fields."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Any

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from vistutils import stringList, searchKey, maybe
from vistutils.fields import AbstractField


class BrushField(AbstractField):
  """BrushField is a descriptor class for QBrush typed fields."""

  @staticmethod
  def _parseKwargs(**kwargs) -> dict[str, Any]:
    """Parsing of keyword arguments"""
    colorKeys = stringList("""colour, color, rgb""")
    colorKwarg = searchKey(QColor, *colorKeys, **kwargs)
    fillKeys = stringList("""style, fillStyle, fill""")
    fillKwarg = searchKey(str, Qt.BrushStyle, *fillKeys, **kwargs)
    return dict(color=colorKwarg, style=fillKwarg)

  @staticmethod
  def _parseArgs(*args) -> dict[str, Any]:
    """Parsing of positional arguments"""
    fillArg, colorArg = None, None
    intArgs = []
    for arg in args:
      if isinstance(arg, QColor) and colorArg is None:
        colorArg = arg
      if isinstance(arg, int):
        if 0 <= arg < 255:
          intArgs.append(arg)
      if isinstance(arg, Qt.BrushStyle) and fillArg is None:
        fillArg = arg
    return dict(color=colorArg, style=fillArg)

  @staticmethod
  def _parse(*args, **kwargs) -> dict[str, Any]:
    """Parsing of arguments"""
    argValues = BrushField._parseArgs(*args)
    colorArg = argValues.get('color')
    styleArg = argValues.get('style')
    kwargValues = BrushField._parseKwargs(**kwargs)
    colorKwarg = kwargValues.get('color')
    styleKwarg = kwargValues.get('style')
    colorDefault = QColor(255, 255, 255, 255)
    styleDefault = Qt.BrushStyle.SolidPattern
    color = maybe(colorKwarg, colorArg, colorDefault)
    style = maybe(styleKwarg, styleArg, styleDefault)
    return dict(color=color, style=style)

  def __init__(self, *args, **kwargs) -> None:
    AbstractField.__init__(self, *args, **kwargs)
    parsed = self._parse(*args, **kwargs)
    self.color = parsed.get('color')
    self.style = parsed.get('style')

  def __prepare_owner__(self, owner: type) -> type:
    """Implementation of method"""
