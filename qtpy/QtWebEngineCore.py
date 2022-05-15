# -----------------------------------------------------------------------------
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""
Provides QtWebEngineCore classes and functions.
"""

from . import PYQT5, PYQT6, PYSIDE2, PYSIDE6, PythonQtError

if PYQT5:
    try:
        from PyQt5.QtWebEngineCore import *
    except ImportError as error:
        raise PythonQtError(
            'The QtWebEngineCore module was not found. '
            'It needs to be installed separately for PyQt5.'
            ) from error
elif PYQT6:
    try:
        from PyQt6.QtWebEngineCore import *
    except ImportError as error:
        raise PythonQtError(
            'The QtWebEngineCore module was not found. '
            'It needs to be installed separately for PyQt6.'
            ) from error
elif PYSIDE2:
    from PySide2.QtWebEngineCore import *
elif PYSIDE6:
    from PySide6.QtWebEngineCore import *
else:
    raise PythonQtError('No Qt bindings could be found')
