"""The SoundEffectList provides a subclass of QListWidget listing the
available sound effects. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os

from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QListWidget
from vistutils.fields import apply

from mediatools import saveAudioFile, __project_root__
from utils import parseParentWidget


class SoundEffectList(QListWidget):
  """The SoundEffectList provides a subclass of QListWidget listing the
  available sound effects. """

  @staticmethod
  def loadEffectsFile() -> list[str]:
    """Loading of sound effects"""
    out = []
    fid = os.path.join(__project_root__, 'sound_effects.data')
    with open(fid, 'r', encoding='utf-8') as file:
      for line in file:
        line = line.strip()
        if not line.startswith('#'):
          if '=' in line:
            out.append(line)
    return out

  @staticmethod
  def parseLine(line: str) -> dict[str, str]:
    """Parses the line"""
    fileName = None
    settings = None
    left, right = None, None
    for (i, char) in enumerate(line):
      if char == '=' and fileName is None:
        fileName = line[:i]
      if char == '[' and left is None:
        left = i
      if char == ']' and right is None:
        right = i
    if isinstance(line, int) and isinstance(right, int):
      settings = line[left + 1:right]
    source = line[right + 1:].strip()
    return dict(fileName=fileName, settings=settings, source=source)

  @classmethod
  def parseSoundEffects(cls, *lines: str) -> dict:
    """Parses the lines to sound effect instances."""
    if len(lines) == 1:
      if isinstance(lines[0], (tuple, list)):
        return cls.parseSoundEffects(*lines[0])
    out = []
    outDict = {}
    for line in lines:
      data = cls.parseLine(line)
      fileName = data.get('fileName', )
      baseFileName = os.path.basename(fileName)
      baseName = os.path.splitext(baseFileName)[0]
      filePath = os.path.join(__project_root__, fileName)
      url = QUrl.fromLocalFile(filePath)
      settings = data.get('settings', None)
      source = data.get('source')
      entry = {'source': source, 'url': url, 'filePath': filePath}
      out.append(entry)
      outDict |= {baseName: entry}
    return outDict

  def __init__(self, *args, **kwargs) -> None:
    parent = parseParentWidget(*args, **kwargs)
    QListWidget.__init__(self, parent)

  def loadSoundEffects(self, ) -> None:
    """Loads the sound effects"""
    lines = self.loadEffectsFile()
    for (key, sound) in self.parseSoundEffects(*lines).items():
      self.addItem(key)

  @apply('currentSound', 'get')
  def _getCurrentSound(self) -> str:
    """Getter-function for the sound effect on the current row."""
    return self.currentItem().text()

  def appendLocalFile(self, localFile: str) -> None:
    """Appends local file defined in arguments creating a new entry. """
    source = os.path.abspath(localFile)
    baseFileName = os.path.basename(localFile)
    baseName = os.path.splitext(baseFileName)[0]
    audioFile = '%s.mp3' % baseName
    audioFilePath = os.path.join(__project_root__, audioFile)
    saveAudioFile(source)
