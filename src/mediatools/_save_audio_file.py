"""Converts mp4 video to mp3 sound"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os.path

from moviepy.editor import VideoFileClip


def saveAudioFile(videoFile: str) -> None:
  """
  Convert an MP4 video file to an MP3 audio file.

  :param videoFile: Path to the input MP4 video file.
  :return: None if successful, error message if unsuccessful.
  """
  root = os.environ['__PROJECT_ROOT__']
  if not os.path.isabs(videoFile):
    videoPath = os.path.join(root, videoFile)
  else:
    videoPath = os.path.abspath(videoFile)
  videoName = os.path.splitext(os.path.basename(videoFile))[0]
  audioFile = '%s.mp3' % videoName
  audioPath = os.path.join(root, audioFile)
  with VideoFileClip(videoPath) as video:
    audio = video.audio
    audio.write_audiofile(audioPath)
