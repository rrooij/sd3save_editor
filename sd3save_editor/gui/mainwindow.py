from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
from datetime import timedelta
from sd3save_editor.gui.mainwindow_ui import Ui_MainWindow
from sd3save_editor.gui.itemtabledelegate import ItemTableDelegate
from sd3save_editor.save import NameTooLongException
import sd3save_editor.save as save
import sd3save_editor.game_data as game_data


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_file_open_events()
        self.init_change_name_input()
        self.ui.storageTableWidget.setItemDelegate(ItemTableDelegate(self))
        self.editedStorageItems = dict()
        self.init_combobox()
        self.show()

    def init_file_open_events(self):
        self.ui.actionOpen.triggered.connect(self.open_file_dialog)

    def set_curr_hp_values(self):
        curr_hp_1 = save.read_current_hp(self.save_file, character_index=0)
        curr_hp_2 = save.read_current_hp(self.save_file, character_index=1)
        curr_hp_3 = save.read_current_hp(self.save_file, character_index=2)
        self.ui.spinBoxCurrentHpChar1.setValue(curr_hp_1)
        self.ui.spinBoxCurrentHpChar2.setValue(curr_hp_2)
        self.ui.spinBoxCurrentHpChar3.setValue(curr_hp_3)

    def set_max_hp_values(self):
        max_hp_1 = save.read_max_hp(self.save_file, character_index=0)
        max_hp_2 = save.read_max_hp(self.save_file, character_index=1)
        max_hp_3 = save.read_max_hp(self.save_file, character_index=2)
        self.ui.spinBoxMaxHpChar1.setValue(max_hp_1)
        self.ui.spinBoxMaxHpChar2.setValue(max_hp_2)
        self.ui.spinBoxMaxHpChar3.setValue(max_hp_3)

    def set_table_data(self):
        items = save.read_all_storage_items_amount(self.save_file)
        self.ui.storageTableWidget.setRowCount(len(items))
        for idx, item in enumerate(items):
            widget_item_name = QTableWidgetItem(item[0])
            widget_item_amount = QTableWidgetItem(str(item[1]))
            self.ui.storageTableWidget.setItem(idx, 0, widget_item_name)
            self.ui.storageTableWidget.setItem(idx, 1, widget_item_amount)
        self.ui.storageTableWidget.itemChanged.connect(self.table_storage_changed)

    def table_storage_changed(self, item):
        self.editedStorageItems[item.row()] = int(item.text())

    def init_change_name_input(self):
        self.ui.c1NameLineEdit.setMaxLength(6)
        self.ui.c2NameLineEdit.setMaxLength(6)
        self.ui.c3NameLineEdit.setMaxLength(6)

    def init_combobox(self):
        self.ui.locationComboBox.addItems(game_data.parse_locations_json())
        self.ui.tracksComboBox.addItems(game_data.parse_tracks_json())

    def init_save_event(self):
        self.ui.actionSave.triggered.connect(self.save_form_values)
        self.ui.saveButton.clicked.connect(self.save_form_values)

    def save_form_values(self):
        location_id = self.ui.locationComboBox.currentIndex() + 1
        track_id = self.ui.tracksComboBox.currentIndex() + 1
        c1Name = self.ui.c1NameLineEdit.text()
        c2Name = self.ui.c2NameLineEdit.text()
        c3Name = self.ui.c3NameLineEdit.text()
        max_hp_1 = self.ui.spinBoxMaxHpChar1.value()
        max_hp_2 = self.ui.spinBoxMaxHpChar2.value()
        max_hp_3 = self.ui.spinBoxMaxHpChar3.value()
        seconds = self.ui.secondsSpinBox.value()
        curr_hp_1 = self.ui.spinBoxCurrentHpChar1.value()
        curr_hp_2 = self.ui.spinBoxCurrentHpChar2.value()
        curr_hp_3 = self.ui.spinBoxCurrentHpChar3.value()
        try:
            save.write_current_music(self.save_file, track_id)
            save.change_location(self.save_file, location_id)
            save.change_character_names(self.save_file, (c1Name, c2Name, c3Name))
            save.write_luc(self.save_file, self.ui.spinBoxLuc.value())
            save.write_max_hp(self.save_file, max_hp_1,
                              character_index=0)
            save.write_max_hp(self.save_file, max_hp_2,
                              character_index=1)
            save.write_max_hp(self.save_file, max_hp_3,
                              character_index=2)
            save.write_current_hp(self.save_file, curr_hp_1,
                                  character_index=0)
            save.write_current_hp(self.save_file, curr_hp_2,
                                  character_index=1)
            save.write_current_hp(self.save_file, curr_hp_3,
                                  character_index=2)
            save.write_time(self.save_file, timedelta(seconds=seconds))
            save.write_storage_item_amounts(self.save_file, self.editedStorageItems)
            QMessageBox.information(self, "Succesfully saved", "Succesfully saved")
        except NameTooLongException as err:
            QMessageBox.warning(self, "Name too long", str(err))
        except OSError as err:
            QMessageBox.warning(self, "Error writing file", str(err))
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
                self.ui.spinBoxLuc.setValue(save.read_luc(self.save_file))
                self.ui.locationComboBox.setCurrentIndex(save.read_location(self.save_file) - 1)
                self.ui.tracksComboBox.setCurrentIndex(save.read_current_music(self.save_file) - 1)
                names = save.read_character_names(self.save_file)
                self.ui.c1NameLineEdit.insert(names[0])
                self.ui.c2NameLineEdit.insert(names[1])
                self.ui.c3NameLineEdit.insert(names[2])
                seconds = int(save.read_time(self.save_file).total_seconds())
                self.ui.secondsSpinBox.setValue(seconds)
                self.set_curr_hp_values()
                self.set_max_hp_values()
                self.set_table_data()
                self.init_save_event()
            except Exception as ex:
                QMessageBox.warning(self, "Can't open Seiken3 save", str(ex))
