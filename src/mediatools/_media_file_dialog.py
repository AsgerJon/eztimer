"""The MediaFileDialog provides a dialog box for selecting an existing
media file. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtWidgets import QFileDialog

from utils import parseParentWidget
from mediatools import __project_root__


class MediaFileDialog(QFileDialog):
  """The MediaFileDialog provides a dialog box for selecting an existing
media file. """

  __media_filter__ = [
    "Video files (*.mp4 *.avi *.mov *.flv *.mkv *.wmv)",
    "Audio files (*.mp3 *.wav *.aac *.flac *.ogg *.wma)",
  ]

  def __init__(self, *args, **kwargs) -> None:
    parent = parseParentWidget(*args, **kwargs)
    QFileDialog.__init__(self, parent)
    self.setDirectory(__project_root__)
    self.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)
    self.setFileMode(QFileDialog.FileMode.ExistingFile)
    self.setNameFilters(self.__media_filter__)
    self.setViewMode(QFileDialog.ViewMode.Detail)
