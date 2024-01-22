"""The MainWindow class subclasses LayoutWindow setting the logic."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os

from PySide6.QtCore import QTimer, QUrl
from PySide6.QtMultimedia import QMediaPlayer, QMediaDevices, QAudioOutput

from windows import __project_root__, LayoutWindow


class MainWindow(LayoutWindow):
  """The MainWindow class subclasses LayoutWindow setting the logic."""

  def __init__(self, *args, **kwargs) -> None:
    LayoutWindow.__init__(self, *args, **kwargs)
    #  Timers
    self._fullTimer = QTimer()
    self._fullTimer.setSingleShot(True)
    self._incrementTimer = QTimer()
    self._incrementTimer.setInterval(100)
    self._incrementTimer.setSingleShot(False)
    #  Actions and signals
    self._fullTimer.timeout.connect(self._timeOutFunc)
    self._incrementTimer.timeout.connect(self._timerUpdateFunc)
    self._startButton.clicked.connect(self._startFunc)
    self._cancelButton.clicked.connect(self._cancelFunc)
    self._timeButton.clicked.connect(self._setTimeFunc)
    self._soundButton.clicked.connect(self._setSoundFunc)
    #  Audio related items
    self._mediaPlayer = QMediaPlayer()
    self._audioDevice = QMediaDevices.defaultAudioOutput()
    self._audioOutput = QAudioOutput(self._audioDevice)
    self._mediaPlayer.setAudioOutput(self._audioOutput)

  def _setMediaSource(self) -> None:
    """Sets up the source for the media player"""
    filePath = None
    for item in os.listdir(__project_root__):
      if os.path.splitext(item)[-1] in ['mp3'] and filePath is None:
        filePath = os.path.join(__project_root__, item)
        self._mediaPlayer.setSource((QUrl.fromLocalFile(filePath)))

  def _timerUpdateFunc(self) -> None:
    """Handles notification of timer update"""
    
  def _startFunc(self, ) -> None:
    """Starts the timer"""

  def _cancelFunc(self, ) -> None:
    """Cancels the timer"""

  def _setTimeFunc(self, ) -> None:
    """Opens the TimeDialog instance allowing for changes to be made to
    the interval of the fullTimer"""

  def _setSoundFunc(self, ) -> None:
    """Opens the sound selection dialog allowing the user to specify a
    particular sound to be played at time out of fullTimer"""

  def _timeOutFunc(self, ) -> None:
    """Resets the fullTimer and starts the alerts."""
