"""The MainWindow class subclasses LayoutWindow setting the logic."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import QTimer
from PySide6.QtMultimedia import QMediaPlayer, QMediaDevices, QAudioOutput

from windows import LayoutWindow


class MainWindow(LayoutWindow):
  """The MainWindow class subclasses LayoutWindow setting the logic."""

  def __init__(self, *args, **kwargs) -> None:
    LayoutWindow.__init__(self, *args, **kwargs)
    self._fullTimer = QTimer()
    self._fullTimer.setSingleShot(True)
    self._fullTimer.timeout.connect(self._timeOutFunc)
    self._incrementTimer = QTimer()
    self._incrementTimer.setInterval(100)
    self._incrementTimer.setSingleShot(False)
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
    here = __project_root__
    self._audioFile = 'rickroll.mp3ttttttttttttttt'

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
