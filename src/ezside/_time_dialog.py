"""TimeDialog opens a modal QDialog with TimeSpinBox. On accept, transmits
the value of the TimeSpin."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog, QVBoxLayout

from ezside import TimeSpin
from utils import parseParentWidget, DialogButtons


class TimeDialog(QDialog):
  """TimeDialog opens a modal QDialog with TimeSpinBox. On accept, transmits
  the value of the TimeSpin."""

  acceptSignal = Signal(int)
  cancelSignal = Signal(int)
  valueChanged = Signal(int)

  def __init__(self, *args, **kwargs) -> None:
    parent = parseParentWidget()
    QDialog.__init__(self, parent, )
    self._timeSpin = TimeSpin()
    self._dialogButtons = DialogButtons()
    self._timeSpin.valueChanged.connect(self._valueChangedEmit)
    self._dialogButtons.cancelClick.connect(self._cancelEmit)
    self._dialogButtons.acceptClick.connect(self._acceptEmit)
    self._baseLayout = QVBoxLayout()

  def _acceptEmit(self, ) -> None:
    """Emits the accept signal"""
    self.acceptSignal.emit(self._timeSpin.value)

  def _cancelEmit(self, ) -> None:
    """Emits the cancel signal"""
    self.cancelSignal.emit(self._timeSpin.value)

  def _valueChangedEmit(self, ) -> None:
    """Emits value change signal"""
    self.valueChanged.emit(self._timeSpin.value)

  def setupWidgets(self) -> None:
    """Sets up the widgets"""
    self._baseLayout.addWidget(self._timeSpin)
    self._baseLayout.addWidget(self._dialogButtons)
    self.setLayout(self._baseLayout)

  def show(self) -> None:
    """Reimplementation"""
    self.setupWidgets()
    QDialog.show(self)
