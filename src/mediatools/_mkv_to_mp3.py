"""Extract audio channel from mkv"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os
# import subprocess
from subprocess import CompletedProcess, run, PIPE

from mediatools import __project_root__, countAudioStreams


def mkv2mp3(mkvFilePath: str, ) -> list[CompletedProcess]:
  """
  Convert a specific audio stream from an MKV file to MP3 format.

  :param mkvFilePath: Path to the input MKV file.
  """
  n = countAudioStreams(mkvFilePath)
  mkvFileName = os.path.basename(mkvFilePath)
  baseName = os.path.splitext(mkvFileName)[0]
  if not os.path.isabs(mkvFilePath):
    mkvFilePath = os.path.join(__project_root__, mkvFileName)
    if not os.path.exists(mkvFilePath):
      raise FileNotFoundError(mkvFileName)
  mkvDir = os.path.dirname(os.path.abspath(mkvFilePath))
  out = []
  n = countAudioStreams(mkvFilePath)
  for i in range(n):
    mp3FileName = '%s_chn_%02d.mp3' % (baseName, i)
    mp3FilePath = os.path.join(mkvDir, mp3FileName)
    cmd = [
      'ffmpeg', '-y', '-i', mkvFilePath,
      '-map', f'0:a:{i}',  # Select the specific audio stream
      '-acodec', 'libmp3lame', '-ar', '44100', '-ac', '2', '-b:a', '192k',
      mp3FilePath
    ]
    res = run(cmd, check=True, text=True, stdout=PIPE, stderr=PIPE, )
    out.append(res)
  return out
