from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QItemDelegate, QLineEdit, QSpinBox


class ItemTableDelegate(QItemDelegate):

    def __init__(self, parent=None):
        super(ItemTableDelegate, self).__init__(parent)
        self.editedValues = []

    def createEditor(self, parent, styleOption, index):
        if index.column() == 0:
            editor = QLineEdit(parent)
            editor.setReadOnly(True)
            return editor
        editor = QSpinBox(parent)
        return editor

    def setEditorData(self, editor, index):
        if isinstance(editor, QLineEdit):
            editor.setText(index.model().data(index, Qt.DisplayRole))
        elif isinstance(editor, QSpinBox):
            value = int(index.model().data(index, Qt.EditRole))
            editor.setValue(value)

    def setModelData(self, editor, model, index):
        if isinstance(editor, QLineEdit):
            model.setData(index, editor.text())
        elif isinstance(editor, QSpinBox):
            model.setData(index, editor.value())
