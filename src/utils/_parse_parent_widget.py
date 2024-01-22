"""The parseParentWidget looks for a QWidget at keyword parent. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Optional

from PySide6.QtWidgets import QWidget
from vistutils import stringList, maybeType, searchKey, maybe


def parseParentWidget(*args, **kwargs) -> Optional[QWidget]:
  """The parseParentWidget looks for a QWidget at keyword parent. """

  parentKeys = stringList("""parent, parentWidget""")
  parentKwarg = searchKey(QWidget, *parentKeys, **kwargs)
  parentArg = maybeType(QWidget, *args)
  parent = maybe(parentKwarg, parentArg)
  if isinstance(parent, QWidget):
    return parent

