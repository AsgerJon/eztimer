"""Main Tester Script"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import sys
import os
from typing import NoReturn

from PySide6.QtWidgets import QApplication
from icecream import ic

from windows import MainWindow
from mediatools import mkv2mp3

ic.configureOutput(includeContext=True)


def tester00() -> None:
  """Hello world!"""
  stuff = [os, sys, ic]
  for item in stuff:
    ic(item)


def tester01() -> None:
  """mp4 to mp3"""
  os.environ['__PROJECT_ROOT__'] = os.path.dirname(os.path.abspath(__file__))
  print(os.environ['__PROJECT_ROOT__'])
  mkv2mp3('oregen.mkv')


def tester02() -> NoReturn:
  """Test of colors"""
  app = QApplication(sys.argv)
  main = MainWindow()
  main.show()
  sys.exit(app.exec())


def tester03() -> NoReturn:
  """Test of file ext"""
  ic(os.path.splitext('lmao'))


if __name__ == "__main__":
  tester02()
