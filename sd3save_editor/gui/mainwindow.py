from PyQt5.QtWidgets import (QMainWindow, QFileDialog,
                             QMessageBox, QTableWidgetItem)

from sd3save_editor.gui.mainwindow_ui import Ui_MainWindow
from sd3save_editor.gui.itemtabledelegate import ItemTableDelegate
from sd3save_editor.gui.datatype import (ComboBoxElement, LineEditElement,
                                         SpinboxElement)
from sd3save_editor.save import NameTooLongException
from sd3save_editor.save import Language
import sd3save_editor.save as save
import sd3save_editor.game_data as game_data

from pathlib import Path
import re


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initFileOpenEvents()
        self.initChangeNameInput()
        self.initLanguageComboBox()
        self.autoLanguage = Language.ENGLISH;
        self.updateLanguageComboBox();
        self.initSaveEvent()
        self.saveIndex = None
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
            "strength": SpinboxElement(
                guiElements=[self.ui.strengthLvlSpinBoxChar1,
                             self.ui.strengthLvlSpinBoxChar2,
                             self.ui.strengthLvlSpinBoxChar3],
                dataKey='data.value.{}.strength',
                dataCharacters=True,
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
        items = save.read_all_storage_items_amount(self.saveData,
                                                   self.saveIndex)
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
        self.ui.c1NameLineEdit.textChanged.connect(self.validateCharacterNames)
        self.ui.c2NameLineEdit.textChanged.connect(self.validateCharacterNames)
        self.ui.c3NameLineEdit.textChanged.connect(self.validateCharacterNames)

    def initLanguageComboBox(self):
        self.ui.languageComboBox.activated.connect(self.languageChanged)

    def updateLanguageComboBox(self):
        text = self.ui.languageComboBox.itemText(self.autoLanguage.value);
        self.ui.languageComboBox.setItemText(0, "Auto -- {}".format(text))

    def languageChanged(self, index):
        if (index == 0):
            save.char_name_language = self.autoLanguage
        else:
            save.char_name_language = Language(index)
        self.validateCharacterNames()

    def validateCharacterNames(self):
        for lineEdit in [
            self.ui.c1NameLineEdit,
            self.ui.c2NameLineEdit,
            self.ui.c3NameLineEdit,
        ]:
            lineEdit.setText(
                save.char_name_adapter.parse(
                    save.char_name_adapter.build(
                        lineEdit.text())))

    def initSaveEntryComboBox(self):
        self.ui.saveIndexComboBox.clear()
        for x in range(0, 3):
            if self.saveData[x]:
                self.ui.saveIndexComboBox.addItem("Save entry {}".
                                                  format(x + 1), x)
        self.ui.saveIndexComboBox.activated.connect(self.saveEntryChanged)

    def saveEntryChanged(self, index):
        saveIndex = self.ui.saveIndexComboBox.itemData(index)
        self.saveIndex = saveIndex
        self.initData()
        self.setTableData()

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
                                            self.editedStorageItems,
                                            self.saveIndex)
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
            self.autoLanguage = self.detectLanguage(Path(self.filename).stem)
            self.updateLanguageComboBox()
            if self.ui.languageComboBox.currentIndex() == 0:
                save.char_name_language = Language(self.autoLanguage.value)
            else:
                save.char_name_language = Language(self.ui.languageComboBox.currentIndex())
        if self.filename:
            try:
                self.saveData = save.read_save(self.filename)
                self.saveIndex = next(index for index,
                                      value in enumerate(self.saveData)
                                      if value is not None)
                self.ui.saveButton.setEnabled(True)
                self.ui.actionSave.setEnabled(True)
                self.initData()
                self.setTableData()
                self.initSaveEntryComboBox()
            except Exception as ex:
                self.ui.saveButton.setEnabled(False)
                self.ui.actionSave.setEnabled(False)
                QMessageBox.warning(self, "Can't open Seiken3 save", str(ex))

    @staticmethod
    def detectLanguage(name):
        # orignal Japanese release
        if (re.search(r"\ASeiken Densetsu 3 \((J|Japan)\)\Z", name, re.IGNORECASE)):
            return Language.JAPANESE
        # translation patches
        if (re.search(r"\A(SD3|SOM2|SEIKEN3)(E|EN|ENG)[0-9]*\Z", name, re.IGNORECASE)):
            return Language.ENGLISH
        if (re.search(r"\A(SD3|SOM2|SEIKEN3)(F|FR|FRA)[0-9]*\Z", name, re.IGNORECASE)):
            return Language.FRENCH
        if (re.search(r"\A(SD3|SOM2|SEIKEN3)(D|G|DE|DEU|GER)[0-9]*\Z", name, re.IGNORECASE)):
            return Language.GERMAN
        if (re.search(r"\A(SD3|SOM2|SEIKEN3)(I|IT|ITA)[0-9]*\Z", name, re.IGNORECASE)):
            return Language.ITALIAN
        if (re.search(r"\A(SD3|SOM2|SEIKEN3)(J|JA|JP|JAP)[0-9]*\Z", name, re.IGNORECASE)):
            return Language.JAPANESE
        if (re.search(r"\A(SD3|SOM2|SEIKEN3)(S|ES|SP|ESP|SPA)[0-9]*\Z", name, re.IGNORECASE)):
            return Language.SPANISH
        # translation patches (Italian exception)
        if (re.search(r"\A(SD3|SOM2|SEIKEN3)_(JAP|ENG)_ITA_", name, re.IGNORECASE)):
            return Language.ITALIAN
        # translation authors
        if (re.search(r"(\A|\W)(neill|corlett|som2freak)(\Z|\W)", name, re.IGNORECASE)):
            return Language.ENGLISH
        if (re.search(r"(\A|\W)(terminus|copernic)\W", name, re.IGNORECASE)):
            return Language.FRENCH
        if (re.search(r"(\A|\W)(g-trans|special-man|lavosspawn)(\Z|\W)", name, re.IGNORECASE)):
            return Language.GERMAN
        if (re.search(r"(\A|\W)(mumble|clomax|ombra|chester)(\Z|\W)", name, re.IGNORECASE)):
            return Language.ITALIAN
        if (re.search(r"(\A|\W)(magno|vegetal|gibber)(\Z|\W)", name, re.IGNORECASE)):
            return Language.SPANISH
        # language codes
        if (re.search(r"(\A|\W)(en|eng|english)(\Z|\W)", name, re.IGNORECASE)):
            return Language.ENGLISH
        if (re.search(r"(\A|\W)(fr|fra|french|français|francais)(\Z|\W)", name, re.IGNORECASE)):
            return Language.FRENCH
        if (re.search(r"(\A|\W)(de|deu|ger|german|deutsch)(\Z|\W)", name, re.IGNORECASE)):
            return Language.GERMAN
        if (re.search(r"(\A|\W)(it|ita|italian|italiano)(\Z|\W)", name, re.IGNORECASE)):
            return Language.ITALIAN
        if (re.search(r"(\A|\W)(ja|jp|jap|japanese)(\Z|\W)", name, re.IGNORECASE)):
            return Language.JAPANESE
        if (re.search(r"(\A|\W)(es|sp|esp|spa|spanish|español|espanol|castellano)(\Z|\W)", name, re.IGNORECASE)):
            return Language.SPANISH
        # fallback
        return Language.ENGLISH

