"""The SoundSelection dialog allows the user to select an existing sound
effect or to create a new sound effect from a file. This  file will be
converted as necessary. The file will then remain available."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog, QGridLayout, QListWidget
from PySide6.QtWidgets import QPushButton, QLineEdit

from mediatools import MediaFileDialog
from utils import parseParentWidget


class SoundSelection(QDialog):
  """The SoundSelection dialog allows the user to select an existing sound
  effect or to create a new sound effect from a file. This  file will be
  converted as necessary. The file will then remain available."""

  mediaFileSelected = Signal(str)

  def __init__(self, *args, **kwargs) -> None:
    parent = parseParentWidget()
    QDialog.__init__(self, parent, )
    self._baseLayout = QGridLayout()
    self._soundList = QListWidget()
    self._mediaFileDialog = MediaFileDialog()
    self._mediaFileDialog.fileSelected.connect(self._handleFile)
    self._loadSoundFileButton = QPushButton('Load')
    self._newSoundLineEdit = QLineEdit()
    self._convertSound = QPushButton('Convert')

  def setupWidgets(self) -> None:
    """Sets up the widgets"""
    self._baseLayout.addWidget(self._soundList, 0, 0, 1, 3)
    self._baseLayout.addWidget(self._loadSoundFileButton, 1, 0, 1, 1)
    self._baseLayout.addWidget(self._newSoundLineEdit, 1, 1, 1, 1)
    self._baseLayout.addWidget(self._convertSound, 1, 2, 1, 1)
    self.setLayout(self._baseLayout)

  def show(self) -> None:
    """Reimplementation inserting setupWidgets before parent method"""
    self.setupWidgets()
    QDialog.show(self)

  def _handleFile(self, file: str = None) -> None:
    """Handles the accepted file from the media file dialog"""
    if file is None:
      return
    if not file:
      return
    if os.path.exists(file):
      self.mediaFileSelected.emit(file)
