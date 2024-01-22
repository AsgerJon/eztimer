"""The windows module provides the classes relating to the main
application window class chain. The module also provides subclasses of
QDialog. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from ._project_root import __project_root__
from ._base_window import BaseWindow
from ._layout_window import LayoutWindow
from ._main_window import MainWindow
