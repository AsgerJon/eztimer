"""Points to project root"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations
import os

here = os.path.dirname(os.path.abspath(__file__))
__project_root__ = os.path.normpath(os.path.join(here, '..', '..'))
