VERSION=0.4
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

clean:
	$(RM) *.deb
