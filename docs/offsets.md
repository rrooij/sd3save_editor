# Offsets

This document should contain most of the offsets I found myself and have collected from other resources.
Each save entry should be seperated by 0x800

## General information

| Name                          | Offset | Length (bytes) |
|-------------------------------+--------+----------------|
| Distance between save entries |  0x800 |                |
| End of first save             |  0x7FD |                |
| Checksum                      |  0x7FE |              2 |
| Player's location             |  0x726 |              2 |
| End of header                 |   0x6F |                |

## Header

The header contains the information you see on the save select screen in the game.
Each save entry has its own header. Information for all three characters are stored
in the header if they are unlocked in the game, seperated by `0x20`. That's why I only
documented the first character, since you just add 0x20 to go to the next character.


| Name                     | Offset |              Length | Description                                                |
|--------------------------+--------+---------------------+------------------------------------------------------------|
| Exist string             |    0x0 |                   5 | Every save header starts with this string, encoded ASCII   |
| 1st character name       |   0x10 |                  12 | Encoded in UTF-16-le, as far as I know. Padded with 0 byte |
| 1st character lvl        |   0x1C |                   1 | For some reason, the real level is the value + 1           |
| 1st character current HP |   0x1D |                   2 |                                                            |
| 1st character max HP     |   0x1F |                   2 |                                                            |
| 1st character current MP |   0x21 |                   2 |                                                            |
| 1st character max MP     |   0x23 |                   2 |                                                            |
| Last selected save       |   0x4E |                   1 | The last chosen save, index starts at 0                    |
| Time                     |   0x6C | 3, but I'm not sure | Time played                                                |
