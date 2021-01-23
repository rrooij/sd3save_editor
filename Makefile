VERSION=0.5.3
PACKAGE_NAME=python3-sd3save-editor_$(VERSION)_all
FOLDER_SEPERATOR=":"
TARGET=dist/sd3save_editor
PYINSTALLER_FLAGS="-F"

ifeq ($(OS),Windows_NT)
	FOLDER_SEPERATOR=";"
	TARGET=dist/sd3save_editor.exe
else ifeq ($(shell uname),Darwin)
	PYINSTALLER_FLAGS=
endif

ifeq ($(OS),Windows_NT)
	FOLDER_SEPERATOR=";"
	TARGET=dist/sd3save_editor.exe
endif

$(TARGET):
	pyinstaller sd3save_editor/gui/__main__.py -n sd3save_editor \
	--add-data "sd3save_editor/data"$(FOLDER_SEPERATOR)"sd3save_editor/data" $(PYINSTALLER_FLAGS)

.PHONY: $(TARGET)

package_deb:
	dpkg-buildpackage -us -uc

7zip_windows:
	7z a dist/windows_exe.7z dist/sd3save_editor

clean:
	$(RM) ../$(PACKAGE_NAME).deb
	$(RM) ../$(PACKAGE_NAME).tar.gz
	$(RM) -r debian/python3-sd3save-editor
	$(RM) -r dist/*
