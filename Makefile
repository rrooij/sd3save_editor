FOLDER_SEPERATOR=":"
TARGET=dist/sd3save_editor

ifeq ($(OS),Windows_NT)
	FOLDER_SEPERATOR=";"
	TARGET=dist/sd3save_editor.exe
endif

$(TARGET):
	pyinstaller sd3save_editor/gui/__main__.py -n sd3save_editor \
	--add-data "sd3save_editor/data"$(FOLDER_SEPERATOR)"sd3save_editor/data" -F

.PHONY: $(TARGET)

clean:
	$(RM) -r dist/*
