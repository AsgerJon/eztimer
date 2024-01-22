"""ColorField provides a descriptor class for QColor typed fields"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Optional, Any

from PySide6.QtGui import QColor
from vistutils import stringList, searchKey, maybe
from vistutils.fields import AbstractField, TypedField


class ColorField(AbstractField):
  """ColorField provides a descriptor class for QColor typed fields"""

  red = TypedField(int, 255)
  green = TypedField(int, 255)
  blue = TypedField(int, 255)
  alpha = TypedField(int, 255)

  __fall_back_color__ = QColor(255, 255, 255, 255)
  __initial_color__ = None

  @staticmethod
  def _parseKwargs(**kwargs) -> Optional[QColor]:
    """Parses keyword arguments"""
    redKeys = stringList("""red, r""")
    redKwarg = searchKey(int, *redKeys, **kwargs)
    greenKeys = stringList("""green, g""")
    greenKwarg = searchKey(int, *greenKeys, **kwargs)
    blueKeys = stringList("""blue, b""")
    blueKwarg = searchKey(int, *blueKeys, **kwargs)
    alphaKeys = stringList("""alpha, a""")
    alphaKwarg = searchKey(int, *alphaKeys, **kwargs)
    rgba = [redKwarg, greenKwarg, blueKwarg, alphaKwarg]
    names = stringList("""red, green, blue, alpha""")
    if all([isinstance(arg, int) for arg in rgba]):
      return QColor(*rgba)

  @staticmethod
  def _parseArgs(*args) -> Optional[QColor]:
    """Parses positional arguments"""
    intArgs = []
    for arg in args:
      if isinstance(arg, QColor):
        return arg
      if isinstance(arg, int):
        if 0 <= arg < 256:
          intArgs.append(arg)
    if len(intArgs) == 1:
      val = intArgs[0]
      return QColor(val, val, val, 255)
    if len(intArgs) == 3:
      return QColor(*intArgs)
    if len(intArgs) > 3:
      return QColor(*intArgs[:4])

  @classmethod
  def _parse(cls, *args, **kwargs) -> QColor:
    """Parses arguments"""
    colorKwarg = cls._parseKwargs(**kwargs)
    colorArg = cls._parseArgs(*args)
    colorDefault = cls.__fall_back_color__
    color = maybe(colorKwarg, colorArg, colorDefault)
    if isinstance(color, QColor):
      return color
    raise TypeError

  def __init__(self, *args, **kwargs) -> None:
    AbstractField.__init__(self, *args, **kwargs)
    color = self._parse(*args, **kwargs)
    self.red = color.red()
    self.green = color.green()
    self.blue = color.blue()
    self.alpha = color.alpha()
    self.__initial_color__ = color

  def _getPrivateName(self, ) -> str:
    """Getter-function for private name"""
    return '_%s' % self.__field_name__

  def __prepare_owner__(self, owner: type) -> None:
    """Implementation of abstract method"""
    pvtName = self._getPrivateName()
    setattr(owner, pvtName, self.__initial_color__)

  def __get__(self, instance: Any, owner: type, **kwargs) -> QColor:
    """Implementation of getter"""
    if instance is None:
      return self.__get__(owner, owner)
    pvtName = self._getPrivateName()
    if hasattr(instance, pvtName, ):
      return getattr(instance, pvtName)
    if kwargs.get('_recursion', False):
      raise RecursionError
    setattr(instance, pvtName, self.__initial_color__)
    return self.__get__(instance, owner, _recursion=True)

  def __set__(self, instance: Any, color: QColor) -> None:
    """Implementation of setter"""
    pvtName = self._getPrivateName()
    if isinstance(color, QColor):
      setattr(instance, pvtName, color)
    if isinstance(color, (tuple, list)):
      parsed = self._parseArgs(*color)
      if isinstance(parsed, QColor):
        color.red = parsed.red()
        color.green = parsed.green()
        color.blue = parsed.alpha()
        color.alpha = parsed.red()
