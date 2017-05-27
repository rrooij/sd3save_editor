from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from sd3save_editor.gui.mainwindow_ui import Ui_MainWindow

from sd3save_editor.save import NameTooLongException
import sd3save_editor.save as save
import sd3save_editor.locations as locations

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_file_open_events()
        self.init_change_name_input()
        self.init_location_combobox()
        self.show()

    def init_file_open_events(self):
        self.ui.actionOpen.triggered.connect(self.open_file_dialog)

    def init_change_name_input(self):
        self.ui.c1NameLineEdit.setMaxLength(6)
        self.ui.c2NameLineEdit.setMaxLength(6)
        self.ui.c3NameLineEdit.setMaxLength(6)

    def init_location_combobox(self):
        self.ui.locationComboBox.addItems(locations.get_locations())

    def init_save_event(self):
        self.ui.actionSave.triggered.connect(self.save_form_values)
        self.ui.saveButton.clicked.connect(self.save_form_values)

    def save_form_values(self):
        location_id = self.ui.locationComboBox.currentIndex() + 1
        save.change_location(self.save_file, location_id)
        c1Name = self.ui.c1NameLineEdit.text()
        c2Name = self.ui.c2NameLineEdit.text()
        c3Name = self.ui.c3NameLineEdit.text()
        try:
            save.change_character_names(self.save_file, (c1Name, c2Name, c3Name))
        except NameTooLongException as err:
            QMessageBox.warning(self, "Name too long", str(err))
        save.write_checksum(self.save_file)
        self.save_file.flush()

    def closeEvent(self, event):
        if hasattr(self, 'save_file'):
            self.save_file.close()
        event.accept()


    def open_file_dialog(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file', filter="Seiken3 Save (*.srm)")[0]
        if filename:
            try:
                self.save_file = save.read_save(filename)
                self.ui.saveButton.setEnabled(True)
                self.ui.actionSave.setEnabled(True)
                self.ui.locationComboBox.setCurrentIndex(save.read_location(self.save_file) - 1)
                names = save.read_character_names(self.save_file)
                self.ui.c1NameLineEdit.insert(names[0])
                self.ui.c2NameLineEdit.insert(names[1])
                self.ui.c3NameLineEdit.insert(names[2])
                self.init_save_event()
            except Exception as ex:
                QMessageBox.warning(self, "Can't open Seiken3 save", str(ex))
