# Seiken Densetsu 3 save editor

Simple save editor made in Python.

It has the following features for now:

* Change luc (the currency in the game)
* Change player names
* Change location

# Running

Clone the repository and run in the folder:

`python3 -m sd3save_editor [options] [file]`

Only Python 3 is supported. View the available locations and their IDs by looking in `sd3save_editor/data/locations.json` with a text editor.

# Running the GUI on Debian or Ubuntu

First, install pyqt and git:

```
sudo apt install python3-pyqt5 git
git clone https://github.com/rrooij/sd3save_editor.git
cd sd3save_editor.git
chmod +x start_gui.sh
./start_gui.sh
```

You can run start_gui.sh afterwards in Nautilus or another file explorer.

# Warning

Backup your save before messing with it!

# Credits

* Location ID's were found [here](https://www.romhacking.net/documents/662/) and made possible by RomHacking.net user [giangurgolo](https://www.romhacking.net/community/801/)
