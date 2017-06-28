from construct import ListContainer
from scalpl import Cut


class DataElement():
    def __init__(self, guiElements, dataKey, headerKey=None,
                 headerCharacters=False, dataCharacters=False, headerType=None,
                 dataType=None):
        self.guiElements = guiElements
        self.dataKey = dataKey
        self.dataType = dataType
        self.headerKey = headerKey
        self.headerCharacters = headerCharacters
        self.dataCharacters = dataCharacters
        self.headerType = headerType

    def setGuiValues(self, saveDataEntry):
        """Set the values for the GUI inputs"""
        proxy = Cut(saveDataEntry)
        for idx, guiElement in enumerate(self.guiElements):
            dataKey = self.dataKey
            if self.dataCharacters:
                dataKey = self._formatCharacterKey(self.dataKey,
                                                   idx)
            value = proxy[dataKey]
            if isinstance(value, ListContainer):
                value = value[idx]
            self._setValue(guiElement, value)

    def setSaveValues(self, saveDataEntry):
        """Set values in the save dictionary from the GUI inputs"""
        proxy = Cut(saveDataEntry)
        dataValueList = []
        headerValueList = []
        for idx, guiElement in enumerate(self.guiElements):
            dataKey = self.dataKey
            if self.dataCharacters:
                dataKey = self._formatCharacterKey(self.dataKey,
                                                   idx)
            value = self._getValue(guiElement)
            if self.dataType is None:
                proxy[dataKey] = value
            elif self.dataType == 'array':
                dataValueList.append(value)
                if idx == 2:  # Stop at latest character
                    proxy[dataKey] = dataValueList
            if self.headerKey:
                headerKey = self.headerKey
                if self.headerCharacters:
                    headerKey = self._formatCharacterKey(self.headerKey,
                                                         idx)
                if self.headerType is None:
                    proxy[headerKey] = value
                elif self.headerType == 'array':
                    headerValueList.append(value)
                    if idx == 2:  # Latest character
                        proxy[headerKey] = headerValueList

    def _formatCharacterKey(self, key, idx):
        return key.format('char' + str(idx + 1))

    def _getValue(self, guiElement):
        raise Exception("Not implemented")

    def _setValue(self, guiElement, value):
        raise Exception("Not implemented")


class SpinboxElement(DataElement):
    def _getValue(self, guiElement):
        return guiElement.value()

    def _setValue(self, guiElement, value):
        guiElement.setValue(value)


class LineEditElement(DataElement):
    def _getValue(self, guiElement):
        return guiElement.text()

    def _setValue(self, guiElement, value):
        guiElement.setText(value)


class ComboBoxElement(DataElement):
    def _getValue(self, guiElement):
        return guiElement.currentIndex() + 1

    def _setValue(self, guiElement, value):
        guiElement.setCurrentIndex(value - 1)
