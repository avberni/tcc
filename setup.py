from cx_Freeze import setup, Executable
import sys
import os

base = None

if sys.platform == 'win32':
    base = None

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

executables = [Executable(script='init.py',base=base)]

packages = ['Windows','numpy']
options = {
    'build_exe': {

        'packages':packages,
        'include_files':[
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
         ]
    },
}

setup(
    name = "SI",
    options = options,
    version = "1.0",
    description = 'Baixa as Imagens',
    executables = executables
)