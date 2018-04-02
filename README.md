# Seiken Densetsu 3 save editor

Simple save editor made in Python.

It has the following features for now:

* Change luc (the currency in the game)
* Change player names
* Change location
* Change max HP and current HP
* View and manipulate player stats
* Change the currently playing audio track
* View and update item inventory

**Please finish the game without cheating first if you planned
  to do this by editing your save.
  The challenge of the game adds up to the experience.**

# Running

Clone the repository and run in the folder:

`python3 -m sd3save_editor [options] [file]`

Only Python 3 is supported. View the available locations and their IDs by looking in `sd3save_editor/data/locations.json` with a text editor.

# Running the GUI on Debian or Ubuntu

First, install pyqt and git:

```
sudo apt install python3-pip python3-pyqt5 git
git clone https://github.com/rrooij/sd3save_editor.git
cd sd3save_editor
pip3 install -r requirements.txt
chmod +x start_gui.sh
./start_gui.sh
```

You can run start_gui.sh afterwards in Nautilus or another file explorer.

There is also a nice .deb file available on the [Releases](https://github.com/rrooij/sd3save_editor/releases) page.

# Running on Windows

Check out the [Releases](https://github.com/rrooij/sd3save_editor/releases) page. It will contain a Windows
binary.

# Warning

Backup your save before messing with it!

# Credits

* Location ID's were found [here](https://www.romhacking.net/documents/662/) and made possible by RomHacking.net user [giangurgolo](https://www.romhacking.net/community/801/)
* Some offsets were also found [here](https://www.gamefaqs.com/snes/588648-seiken-densetsu-3/faqs/9788) 
  by GameFAQs user [DavieZBOY](https://www.gamefaqs.com/community/DavieZBOY)
