VERSION=0.5.1
PACKAGE_NAME=python3-sd3save-editor_$(VERSION)_all

.PHONY: package_deb

package_deb:
	dpkg-buildpackage -us -uc

7zip_windows: package_exe
	7z a dist/windows_exe.7z dist/sd3save_editor

package_exe:
	export WINEPREFIX=venv_wine
	wine pyinstaller sd3save_editor/gui/main.py -D	\
	     --paths venv_wine/drive_c/users/$(USER)/Local\ Settings/Application\ Data/Programs/Python/Python35-32/Lib/site-packages/PyQt5/Qt/bin/	\
	     --paths venv_wine/drive_c/users/$(USER)/Local\ Settings/Application\ Data/Programs/Python/Python35-32/	\
	     --name sd3save_editor
	mkdir -p dist/sd3save_editor/sd3save_editor/data
	cp -r sd3save_editor/data dist/sd3save_editor/sd3save_editor/

clean:
	$(RM) *.deb
	$(RM) -r dist/*
