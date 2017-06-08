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
        self.initFileOpenEvents()
        self.initChangeNameInput()
        self.ui.storageTableWidget.setItemDelegate(ItemTableDelegate(self))
        self.editedStorageItems = dict()
        self.initComboBox()
        self.show()

    def initFileOpenEvents(self):
        self.ui.actionOpen.triggered.connect(self.openFileDialog)

    def setCurrentHpValues(self):
        currentHp1 = save.read_current_hp(self.saveFile, character_index=0)
        currentHp2 = save.read_current_hp(self.saveFile, character_index=1)
        currentHp3 = save.read_current_hp(self.saveFile, character_index=2)
        self.ui.spinBoxCurrentHpChar1.setValue(currentHp1)
        self.ui.spinBoxCurrentHpChar2.setValue(currentHp2)
        self.ui.spinBoxCurrentHpChar3.setValue(currentHp3)

    def setMaxHpValues(self):
        maxHp1 = save.read_max_hp(self.saveFile, character_index=0)
        maxHp2 = save.read_max_hp(self.saveFile, character_index=1)
        maxHp3 = save.read_max_hp(self.saveFile, character_index=2)
        self.ui.spinBoxMaxHpChar1.setValue(maxHp1)
        self.ui.spinBoxMaxHpChar2.setValue(maxHp2)
        self.ui.spinBoxMaxHpChar3.setValue(maxHp3)

    def setTableData(self):
        items = save.read_all_storage_items_amount(self.saveFile)
        self.ui.storageTableWidget.setRowCount(len(items))
        for idx, item in enumerate(items):
            itemNameWidget = QTableWidgetItem(item[0])
            itemAmountWidget = QTableWidgetItem(str(item[1]))
            self.ui.storageTableWidget.setItem(idx, 0, itemNameWidget)
            self.ui.storageTableWidget.setItem(idx, 1, itemAmountWidget)
        self.ui.storageTableWidget.itemChanged.connect(self.tableStorageChanged)

    def tableStorageChanged(self, item):
        self.editedStorageItems[item.row()] = int(item.text())

    def initChangeNameInput(self):
        self.ui.c1NameLineEdit.setMaxLength(6)
        self.ui.c2NameLineEdit.setMaxLength(6)
        self.ui.c3NameLineEdit.setMaxLength(6)

    def initComboBox(self):
        self.ui.locationComboBox.addItems(game_data.parse_locations_json())
        self.ui.tracksComboBox.addItems(game_data.parse_tracks_json())

    def initSaveEvent(self):
        self.ui.actionSave.triggered.connect(self.saveFormValues)
        self.ui.saveButton.clicked.connect(self.saveFormValues)

    def saveFormValues(self):
        locationId = self.ui.locationComboBox.currentIndex() + 1
        trackId = self.ui.tracksComboBox.currentIndex() + 1
        c1Name = self.ui.c1NameLineEdit.text()
        c2Name = self.ui.c2NameLineEdit.text()
        c3Name = self.ui.c3NameLineEdit.text()
        maxHp1 = self.ui.spinBoxMaxHpChar1.value()
        maxHp2 = self.ui.spinBoxMaxHpChar2.value()
        maxHp3 = self.ui.spinBoxMaxHpChar3.value()
        seconds = self.ui.secondsSpinBox.value()
        currentHp1 = self.ui.spinBoxCurrentHpChar1.value()
        currentHp2 = self.ui.spinBoxCurrentHpChar2.value()
        currentHp3 = self.ui.spinBoxCurrentHpChar3.value()
        try:
            save.write_current_music(self.saveFile, trackId)
            save.change_location(self.saveFile, locationId)
            save.change_character_names(self.saveFile, (c1Name, c2Name, c3Name))
            save.write_luc(self.saveFile, self.ui.spinBoxLuc.value())
            save.write_max_hp(self.saveFile, maxHp1,
                              character_index=0)
            save.write_max_hp(self.saveFile, maxHp2,
                              character_index=1)
            save.write_max_hp(self.saveFile, maxHp3,
                              character_index=2)
            save.write_current_hp(self.saveFile, currentHp1,
                                  character_index=0)
            save.write_current_hp(self.saveFile, currentHp2,
                                  character_index=1)
            save.write_current_hp(self.saveFile, currentHp3,
                                  character_index=2)
            save.write_time(self.saveFile, timedelta(seconds=seconds))
            save.write_storage_item_amounts(self.saveFile, self.editedStorageItems)
            QMessageBox.information(self, "Succesfully saved", "Succesfully saved")
        except NameTooLongException as err:
            QMessageBox.warning(self, "Name too long", str(err))
        except OSError as err:
            QMessageBox.warning(self, "Error writing file", str(err))
        save.write_checksum(self.saveFile)
        self.saveFile.flush()

    def closeEvent(self, event):
        if hasattr(self, 'saveFile'):
            self.saveFile.close()
        event.accept()


    def openFileDialog(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file', filter="Seiken3 Save (*.srm)")[0]
        if filename:
            try:
                self.saveFile = save.read_save(filename)
                self.ui.saveButton.setEnabled(True)
                self.ui.actionSave.setEnabled(True)
                self.ui.spinBoxLuc.setValue(save.read_luc(self.saveFile))
                self.ui.locationComboBox.setCurrentIndex(save.read_location(self.saveFile) - 1)
                self.ui.tracksComboBox.setCurrentIndex(save.read_current_music(self.saveFile) - 1)
                names = save.read_character_names(self.saveFile)
                self.ui.c1NameLineEdit.insert(names[0])
                self.ui.c2NameLineEdit.insert(names[1])
                self.ui.c3NameLineEdit.insert(names[2])
                seconds = int(save.read_time(self.saveFile).total_seconds())
                self.ui.secondsSpinBox.setValue(seconds)
                self.setCurrentHpValues()
                self.setMaxHpValues()
                self.setTableData()
                self.initSaveEvent()
            except Exception as ex:
                QMessageBox.warning(self, "Can't open Seiken3 save", str(ex))
