"""The countAudioChannels method receives a media file and returns the
number of audio channels present."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import subprocess
import json
from typing import Union


def countAudioStreams(videoFilePath: str) -> Union[int, str]:
  """
  Count the number of audio streams in a video file using ffprobe.

  :param videoFilePath: Path to the video file.
  :return: Number of audio streams if successful, error message if an
  error occurs.
  """
  # ffprobe command to get stream information in JSON format
  cmd = [
    'ffprobe',
    '-v', 'error',
    '-select_streams', 'a',  # Select only audio streams
    '-show_entries', 'stream=index',
    '-of', 'json',
    videoFilePath
  ]

  # Execute the command and capture the output
  result = subprocess.run(cmd,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          text=True)
  output = json.loads(result.stdout)

  # Count the number of audio streams
  audio_streams = output.get('streams', [])
  return len(audio_streams)
