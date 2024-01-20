"""Main Tester Script"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import sys
import os

from icecream import ic

ic.configureOutput(includeContext=True)


def tester00() -> None:
  """Hello world!"""
  stuff = [os, sys, ic]
  for item in stuff:
    ic(item)


if __name__ == "__main__":
  tester00()
