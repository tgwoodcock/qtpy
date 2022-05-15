# -----------------------------------------------------------------------------
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""
Provides Windows-specific utilities
"""

import platform
from . import PYQT5, PYQT6, PYSIDE2, PYSIDE6, PythonQtError

if platform.system() == 'Windows':
    if PYQT5:
        from PyQt5.QtWinExtras import *
    elif PYQT6:
        raise PythonQtError('QtWinExtras does not exist in Qt6')
    elif PYSIDE2:
        from PySide2.QtWinExtras import *
    elif PYSIDE6:
        raise PythonQtError('QtWinExtras does not exist in Qt6')
    else:
        raise PythonQtError('No Qt bindings could be found')
else:
    raise PythonQtError('QtWinExtras does not exist on this operating system')
