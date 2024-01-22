"""OverloadMeta provides a metaclass allowing derived classes to overload
methods. The overload decorator should be called with a signature to
indicate to the dispatcher, what signature the decorated function
supports. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from vistutils.metas import AbstractMetaclass


class OverloadMeta(AbstractMetaclass):
  """OverloadMeta provides a metaclass allowing derived classes to overload
  methods. The overload decorator should be called with a signature to
  indicate to the dispatcher, what signature the decorated function
  supports. """
