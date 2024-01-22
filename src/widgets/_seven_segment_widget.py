"""The SevenSegmentWidget subclasses QLCDNumber. It contains an inner
value of type str that it displays."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from warnings import warn

from PySide6.QtWidgets import QLCDNumber
from vistutils import maybe, maybeType, searchKey
from vistutils.fields import apply

from utils import parseParentWidget, CustomField


class SevenSegmentWidget(QLCDNumber):
  """The SevenSegmentWidget subclasses QLCDNumber. It contains an inner
  value of type str that it displays."""

  message = CustomField()

  def __init__(self, *args, **kwargs) -> None:
    parent = parseParentWidget(*args, **kwargs)
    digitsKwarg = searchKey(int, 'digits', 'n', **kwargs)
    digitsArg = maybeType(int, *args)
    digitsDefault = 5
    digits = maybe(digitsKwarg, digitsArg, digitsDefault)
    msgKwarg = searchKey(str, 'msg', 'message', **kwargs)
    msgArg = maybeType(str, *args)
    msgDefault = '13:37'
    msg = maybe(msgKwarg, msgArg, msgDefault)
    if isinstance(msg, str):
      self.__inner_message__ = msg
    else:
      raise TypeError
    QLCDNumber.__init__(self, digits, parent)

  @apply('message', 'get')
  def _getMessage(self) -> str:
    """Getter-function for message"""
    return self.__inner_message__

  @apply('message', 'set')
  def _setMessage(self, message: str) -> None:
    """Setter-function for message"""
    oldMessage = self.message
    try:
      if len(message) != self.digitCount():
        self.setDigitCount(len(message))
      self.display(message)
      self.update()
      self.__inner_message__ = message
    except Exception as exception:
      e = """During call to the setter-function, instance '%s' 
      encountered: exception: '%s'. Old value: '%s' is restored and 
      attempted new value: '%s' is rejected!"""
      warn(e % (self, exception, oldMessage, message))
      self.__inner_message__ = oldMessage
