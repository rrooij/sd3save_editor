from PyQt5.QtWidgets import (QComboBox, QMainWindow, QFileDialog, QLineEdit,
                             QMessageBox, QSpinBox, QTableWidgetItem)
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
        self.saveIndex = 0  # TODO let the user decide this
        self.guiData = {
            "currentHp": {
                "gui": [self.ui.spinBoxCurrentHpChar1,
                        self.ui.spinBoxCurrentHpChar2,
                        self.ui.spinBoxCurrentHpChar3],
                "data": lambda self: [self.saveData[self.saveIndex].data.value.char1.current_hp,
                                      self.saveData[self.saveIndex].data.value.char2.current_hp,
                                      self.saveData[self.saveIndex].data.value.char3.current_hp],
            },
            "maxHp": {
                "gui": [self.ui.spinBoxMaxHpChar1,
                        self.ui.spinBoxMaxHpChar2,
                        self.ui.spinBoxMaxHpChar3],
                "data": lambda self: [self.saveData[self.saveIndex].data.value.char1.max_hp,
                                      self.saveData[self.saveIndex].data.value.char2.max_hp,
                                      self.saveData[self.saveIndex].data.value.char3.max_hp]
            },
            "secondsPlayed": {
                "gui": [self.ui.secondsSpinBox],
                "data": lambda self: [self.saveData[self.saveIndex].header.time_played]
            },
            "luc": {
                "gui": [self.ui.spinBoxLuc],
                "data": lambda self: [self.saveData[self.saveIndex].data.value.luc]
            },
            "names": {
                "gui": [self.ui.c1NameLineEdit, self.ui.c2NameLineEdit, self.ui.c3NameLineEdit],
                "data": lambda self: self.saveData[self.saveIndex].data.value.character_names
            },
            "location": {
                "gui": [self.ui.locationComboBox],
                "data": lambda self: [self.saveData[self.saveIndex].data.value.location - 1]
            },
            "track": {
                "gui": [self.ui.tracksComboBox],
                "data": lambda self: [self.saveData[self.saveIndex].header.playing_music - 1]
            }
        }
        self.ui.storageTableWidget.setItemDelegate(ItemTableDelegate(self))
        self.editedStorageItems = dict()
        self.initComboBox()
        self.show()

    def initData(self):
        for entry in self.guiData.values():
            data = entry['data'](self)
            gui = entry['gui']
            for idx, guiElement in enumerate(gui):
                if isinstance(guiElement, QSpinBox):
                    guiElement.setValue(data[idx])
                elif isinstance(guiElement, QLineEdit):
                    guiElement.setText(data[idx])
                elif isinstance(guiElement, QComboBox):
                    guiElement.setCurrentIndex(data[idx])

    def initFileOpenEvents(self):
        self.ui.actionOpen.triggered.connect(self.openFileDialog)

    def setTableData(self):
        self.ui.storageTableWidget.blockSignals(True)
        items = save.read_all_storage_items_amount(self.saveData)
        self.ui.storageTableWidget.setRowCount(len(items))
        for idx, item in enumerate(items):
            itemNameWidget = QTableWidgetItem(item[0])
            itemAmountWidget = QTableWidgetItem(str(item[1]))
            self.ui.storageTableWidget.setItem(idx, 0, itemNameWidget)
            self.ui.storageTableWidget.setItem(idx, 1, itemAmountWidget)
        self.ui.storageTableWidget.itemChanged.connect(
            self.tableStorageChanged
        )
        self.ui.storageTableWidget.blockSignals(False)

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
        names = [self.ui.c1NameLineEdit.text(),
                 self.ui.c2NameLineEdit.text(),
                 self.ui.c3NameLineEdit.text()]
        maxHp1 = self.ui.spinBoxMaxHpChar1.value()
        maxHp2 = self.ui.spinBoxMaxHpChar2.value()
        maxHp3 = self.ui.spinBoxMaxHpChar3.value()
        seconds = self.ui.secondsSpinBox.value()
        currentHp1 = self.ui.spinBoxCurrentHpChar1.value()
        currentHp2 = self.ui.spinBoxCurrentHpChar2.value()
        currentHp3 = self.ui.spinBoxCurrentHpChar3.value()
        try:
            self.saveData[self.saveIndex].header.playing_music = trackId
            self.saveData[self.saveIndex].data.value.location = locationId
            save.write_character_names(self.saveData,
                                       names,
                                       self.saveIndex)
            self.saveData[self.saveIndex].data.value.luc = (self.ui
                                                                .spinBoxLuc
                                                                .value())
            self.saveData[self.saveIndex].data.value.char1.max_hp = maxHp1
            self.saveData[self.saveIndex].data.value.char2.max_hp = maxHp2
            self.saveData[self.saveIndex].data.value.char3.max_hp = maxHp3
            self.saveData[self.saveIndex].data.value.char1.current_hp = currentHp1
            self.saveData[self.saveIndex].data.value.char2.current_hp = currentHp2
            self.saveData[self.saveIndex].data.value.char3.current_hp = currentHp3
            self.saveData[self.saveIndex].header.time_played = seconds
            save.write_storage_item_amounts(self.saveData,
                                            self.editedStorageItems)
            save.write_save(self.filename, self.saveData)
            QMessageBox.information(self, "Succesfully saved",
                                          "Succesfully saved")
        except NameTooLongException as err:
            QMessageBox.warning(self, "Name too long", str(err))
        except OSError as err:
            QMessageBox.warning(self, "Error writing file", str(err))

    def openFileDialog(self):
        self.saveData = None  # Clean up previous data
        self.filename = (QFileDialog
                         .getOpenFileName(self,
                                          'Open file',
                                          filter="Seiken3 Save (*.srm)"
                                          ))[0]
        if self.filename:
            try:
                self.saveData = save.read_save(self.filename)
                self.ui.saveButton.setEnabled(True)
                self.ui.actionSave.setEnabled(True)
                self.initData()
                self.setTableData()
                self.initSaveEvent()
            except Exception as ex:
                QMessageBox.warning(self, "Can't open Seiken3 save", str(ex))
