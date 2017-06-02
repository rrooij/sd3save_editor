.PHONY: package_deb
package_deb:
	fpm -s python -d python3-pyqt5 --python-bin=python3 -t deb setup.py
