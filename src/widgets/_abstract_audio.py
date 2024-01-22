"""AudioWidget provides a widget interface to play sounds. To create an
audible widget, subclass this widget. Subclasses must implement the
sound sources. In the simplest case, a subclass might have one or more
sounds that are shared between all instances. More complicated potential
uses might be dynamically changing sounds that are unique to each
instance. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from abc import abstractmethod

from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QAudioDevice
from PySide6.QtMultimedia import QMediaDevices
from PySide6.QtWidgets import QWidget
from vistutils.fields import apply

from utils import parseParentWidget, CustomField


class AbstractAudio(QWidget):
  """AudioWidget provides a widget interface to play sounds. QWidget is not
  required for audio, but as a subclass of QWidget, widgets can implement
  sound effects by subclassing this class. """

  defaultDevice = CustomField()
  audioOutput = CustomField()
  player = CustomField()

  def __init__(self, *args, **kwargs) -> None:
    parent = parseParentWidget(*args, **kwargs)
    QWidget.__init__(self, parent, )
    self.__audio_output__ = None
    self.__media_player__ = None

  @abstractmethod
  def initializePlayer(self) -> None:
    """Subclasses must implement this method. It is invoked as part of the
    show method, and the media player must have a source after this
    method is invoked."""

  def playSound(self) -> None:
    """Plays the current sound"""
    self.player.play()

  def stopSound(self) -> None:
    """Stops the current sound"""
    self.player.stop()

  @staticmethod
  @apply('defaultDevice', 'get')
  def _getDefaultDevice() -> QAudioDevice:
    """Getter-function for the default audio device."""
    return QMediaDevices.defaultAudioOutput()

  @apply('audioOutput', 'get')
  def _getAudioOutput(self) -> QAudioOutput:
    """Getter-function for the audio output."""
    if self.__audio_output__ is None:
      self.__audio_output__ = QAudioOutput(self.defaultDevice)
    return self.__audio_output__

  @apply('player', 'get')
  def _getPlayer(self) -> QMediaPlayer:
    """Getter-function for media player"""
    if self.__media_player__ is None:
      self.__media_player__ = QMediaPlayer()
      self.__media_player__.setAudioOutput(self.audioOutput)
    return self.__media_player__
