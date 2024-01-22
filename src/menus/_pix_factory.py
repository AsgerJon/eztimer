"""The pixFactory function returns instances of QPixmap for use as icons."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os

from PySide6.QtGui import QIcon, QPixmap
from vistutils import stringList
from menus import __project_root__

Icon = QPixmap | QIcon


def _getFileName(name: str, **kwargs) -> str:
  """Loads the file with given name as QPixmap"""
  if not os.path.isabs(name):
    if kwargs.get('_recursion', True):
      raise RecursionError
    name = os.path.join(__project_root__, 'icons', name)
    return _getFileName(name, _recursion=True)
  return name


def pixFactory(name: str, *args, **kwargs) -> QPixmap:
  """The pixFactory function returns instances of QPixmap for use as
  icons."""

  iconTypeArg = None
  for arg in args:
    if arg is QPixmap and iconTypeArg is None:
      iconTypeArg = QPixmap
    if arg is QIcon and iconTypeArg is None:
      iconTypeArg = QIcon

  names = stringList("""new, open, save, save as, cut, copy, 
    paste, about qt, about conda, about python""")

  if name not in names:
    name = 'risitas'

