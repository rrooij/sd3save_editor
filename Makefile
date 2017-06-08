VERSION=0.5
PACKAGE_NAME=python3-sd3save-editor_$(VERSION)_all

.PHONY: package_deb
package_deb:
	fpm -s python -d python3-pyqt5 --python-bin=python3 --python-package-name-prefix python3 -t deb setup.py
	mkdir tmp_extracted
	dpkg-deb -R $(PACKAGE_NAME).deb tmp_extracted
	mkdir -p tmp_extracted/usr/share/applications
	cp sd3save_editor.desktop tmp_extracted/usr/share/applications/
	dpkg-deb -b tmp_extracted $(PACKAGE_NAME).deb
	rm -rf tmp_extracted

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
