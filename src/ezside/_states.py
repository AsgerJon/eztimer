"""The States Enum class specifies the possible states of the timer."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from enum import Enum


class State(Enum):
  """The States Enum class specifies the possible states of the timer."""

  READY = 0  # Before timer start
  RUNNING = 1  # Timer is running and counting down
  ALERTING = 2  # Alerting that time has elapsed
