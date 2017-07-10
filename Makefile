VERSION=0.5.2
PACKAGE_NAME=python3-sd3save-editor_$(VERSION)_all

.PHONY: package_deb

package_deb:
	dpkg-buildpackage -us -uc

7zip_windows: package_exe
	7z a dist/windows_exe.7z dist/sd3save_editor

clean:
	$(RM) *.deb
	$(RM) -r dist/*
