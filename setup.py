from cx_Freeze import setup, Executable

exclude = ['PyQt5.QAxContainer',
           'PyQt5.QtBluetooth',
           'PyQt5.QtHelp',
           'PyQt5.QtLocation',
           'PyQt5.QtMultimedia',
           'PyQt5.QtNetwork',
           'PyQt5.QtQml',
           'PyQt5.QtQuick',
           'PyQt5.QtQuickWidgets',
           'PyQt5.QtGui',
           'PyQt5.QtSensors',
           'PyQt5.QtSerialPort',
           'PyQt5.QtSql',
           'PyQt5.QtSvg',
           'PyQt5.QtWebChannel',
           'PyQt5.QtWebEngine',
           'PyQt5.QtWebEngineWidgets',
           'PyQt5.QtWebKit',
           'PyQt5.QtWebKitWidgets',
           'PyQt5.WebSockets',
           'PyQt5.QtXml',
           'PyQt5.QtXmlPatterns',
           'PyQt5.uic',
           'email',
           'html',
           'tkinter',
           'xml']
buildOptions = dict(packages = [], excludes = exclude)

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('sd3save_editor/gui/main.py', base=base, targetName = 'sd3save_editor_gui'),
    Executable('sd3save_editor/__main__.py', base=base, targetName = 'sd3save_editor_cli')
]

setup(name='sd3save_editor',
      author='rrooij',
      author_email='rderooij685@gmail.com',
      url='https://github.com/rrooij/sd3save_editor',
      version = '0.1',
      license = "GPL-3.0",
      description = 'Seiken Densetsu 3 Save Editor',
      options = dict(build_exe = buildOptions),
      executables = executables)
