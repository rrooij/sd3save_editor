from PyQt5.QtWidgets import (QMainWindow, QFileDialog,
                             QMessageBox, QTableWidgetItem)

from sd3save_editor.gui.mainwindow_ui import Ui_MainWindow
from sd3save_editor.gui.itemtabledelegate import ItemTableDelegate
from sd3save_editor.gui.datatype import (ComboBoxElement, LineEditElement,
                                         SpinboxElement)
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
            "currentHp": SpinboxElement(
                guiElements=[self.ui.spinBoxCurrentHpChar1,
                             self.ui.spinBoxCurrentHpChar2,
                             self.ui.spinBoxCurrentHpChar3],
                dataKey='data.value.{}.current_hp',
                headerKey='header.{}.current_hp',
                headerCharacters=True,
                dataCharacters=True
            ),
            "currentMp": SpinboxElement(
                guiElements=[self.ui.spinBoxCurrMpChar1,
                             self.ui.spinBoxCurrMpChar2,
                             self.ui.spinBoxCurrMpChar3],
                dataKey='data.value.{}.current_mp',
                headerKey='header.{}.current_mp',
                headerCharacters=True,
                dataCharacters=True
            ),
            "maxHp": SpinboxElement(
                guiElements=[self.ui.spinBoxMaxHpChar1,
                             self.ui.spinBoxMaxHpChar2,
                             self.ui.spinBoxMaxHpChar3],
                dataKey='data.value.{}.max_hp',
                headerKey='header.{}.max_hp',
                headerCharacters=True,
                dataCharacters=True
            ),
            "maxMp": SpinboxElement(
                guiElements=[self.ui.spinBoxMaxMpChar1,
                             self.ui.spinBoxMaxMpChar2,
                             self.ui.spinBoxMaxMpChar3],
                dataKey='data.value.{}.max_mp',
                headerKey='header.{}.max_mp',
                headerCharacters=True,
                dataCharacters=True
            ),
            "secondsPlayed": SpinboxElement(
                guiElements=[self.ui.secondsSpinBox],
                dataKey='header.time_played',
            ),
            "luc": SpinboxElement(
                guiElements=[self.ui.spinBoxLuc],
                dataKey='data.value.luc',
            ),
            "names": LineEditElement(
                guiElements=[self.ui.c1NameLineEdit,
                             self.ui.c2NameLineEdit,
                             self.ui.c3NameLineEdit],
                dataKey='data.value.character_names',
                headerKey='header.{}.name',
                # False because the value is an array
                headerCharacters=True,
                dataCharacters=False,
                dataType='array'
            ),
            "location": ComboBoxElement(
                guiElements=[self.ui.locationComboBox],
                dataKey='data.value.location',
            ),
            "track": ComboBoxElement(
                guiElements=[self.ui.tracksComboBox],
                dataKey='header.playing_music',
            )
        }
        self.ui.storageTableWidget.setItemDelegate(ItemTableDelegate(self))
        self.editedStorageItems = dict()
        self.initComboBox()
        self.show()

    def initData(self):
        for guiData in self.guiData.values():
            guiData.setGuiValues(self.saveData[self.saveIndex])

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

    def saveGuiData(self):
        for guiData in self.guiData.values():
            guiData.setSaveValues(self.saveData[self.saveIndex])

    def saveFormValues(self):
        try:
            self.saveGuiData()
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
