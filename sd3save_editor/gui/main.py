#!/usr/bin/env python3

import sys

from PyQt5.QtWidgets import QApplication
from sd3save_editor.gui.mainwindow import MainWindow


app = QApplication(sys.argv)
mainwindow = MainWindow()
sys.exit(app.exec_())
