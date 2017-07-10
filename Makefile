VERSION=0.5.2
PACKAGE_NAME=python3-sd3save-editor_$(VERSION)_all

.PHONY: package_deb

package_deb:
	dpkg-buildpackage -us -uc

7zip_windows: package_exe
	7z a dist/windows_exe.7z dist/sd3save_editor

clean:
	$(RM) ../$(PACKAGE_NAME).deb
	$(RM) ../$(PACKAGE_NAME).tar.gz
	$(RM) -r debian/python3-sd3save-editor
	$(RM) -r dist/*
