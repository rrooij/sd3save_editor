# Language Support

- Original Japanese Release
- English Translation V1.01 by Neill Corlett 
- French Translation RC1 by Terminus Traduction
- German Translation V1.00 RC3 to V3.0 by G-Trans
- Italian Translation V1.00b  by Clomax, Ombra, Chester
- Spanish Translation V1.03 by Magno, Vegetal Gibber

## UI Changes

You can select the language of the cartridge from the combo box at the top. Unfortunately, there is no way to automatically detect the language from just the save file.

It is recommended to choose the right language before loading the save file. If you change the language afterwards, the current player names will automatically be mapped to the new encoding, leading to a possible drop of unsupported characters. If this happens, just load the save file again.

Also, the program will check for unsupported characters on input, which means you can only input valid characters for the currently selected language. For compatibility both half-width and full-width characters are supported.

Besides, most ASCII characters are present in all language encodings.

A player's name is limited to a maximum length of 6 characters.

## Remarks

There are currently two encoding files for Japanese to Unicode: One with full-width encoding and the other with half-width encoding in Unicode. Both work equally well. For now I went with full-width.

You can change this by simply overwriting `encoding_japanese_to_unicode.json` with either `encoding_japanese_to_unicode_halfwidth.json` or `encoding_japanese_to_unicode_fullwidth.json`.

Besides, when converting from Unicode to Japanese, both half-width and full-width characters are supported regardlessly.

## Known Issues

- The Italian and the Spanish cartridge encoding both have a codepoint for the double L (ll). However, there is no according Unicode codepoint for it.

