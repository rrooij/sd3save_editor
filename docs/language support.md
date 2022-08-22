# Language Support

- Original Japanese Release
- English Translation V1.01 by Neill Corlett, SoM2Freak
- French Translation RC1 by Terminus Traduction (Copernic)
- German Translation V1.00 RC3 to V3.0 by G-Trans (Special-Man, LavosSpawn)
- Italian Translation V1.00b by Mumble Translations (Clomax, Ombra, Chester)
- Spanish Translation V1.03 by Magno, Vegetal Gibber

## Automatic Language Detection

The filename is being used to determine the translation patch. Unfortunately, there is no way to detect the translation patch from the save file data directly, so the filename has to suffice.

Please refer to the source code for the actual regular expressions.

### Detection Order

1. Original Japanese ROM name without any translation information (Japanese)

    | | |
    | ---| --- |
    | **Japanese** | Seiken Densetsu 3 (J) <br/> Seiken Densetsu 3 (Japan) |

2. Patch name (English, French, German, Italian, Spanish, incl. Japanese)

    | | |
    | ---| --- |
    | **English** | SD3EN101.IPS |
    | **French** | SEIKEN3F.IPS |
    | **German** | SEIKEN3D.IPS <br/> SD3GER203.IPS <br/> SD3DE30.IPS |
    | **Italian** | SD3_JAP_ITA_V100_BETA_6A93E9F.IPS <br/> SD3_ENG_ITA_V100_BETA_6A93E9F.IPS |
    | **Spanish** | SOM2SP.IPS |

    So, either one of `SD3` or `SOM2` or `SEIKEN3`, followed by a one to three letter language code, followed by an optional version number.

    Only Italian differs from this pattern slightly.

3. Translator / translation team (English, French, German, Italian, Spanish)

    | | |
    | ---| --- |
    | **English** | Neill Corlett, SoM2Freak |
    | **French** | Terminus Traduction, Copernic |
    | **German** | G-Trans, Special-Man, LavosSpawn |
    | **Italian** | Mumble Translations, Clomax, Ombra, Chester |
    | **Spanish** | Magno, Vegetal Gibber |

4. Language / language code (English, French, German, Italian, Spanish, incl. Japanese)

    | | |
    | ---| --- |
    | **English** | en, eng, english |
    | **French** | fr, fra, french, français, francais |
    | **German** | de, deu, ger, german, deutsch |
    | **Italian** | it, ita, italian, italiano |
    | **Japanese** | ja, jp, jap, japanese |
    | **Spanish** | es, sp, esp, spa, spanish, español, espanol, castellano |

    Only two and three letter language codes are taken into account here, no single letter codes.

5. Fallback to English

### Remarks

- File names are treated case-insensitive.
- There is also a pre-patched ROM circulating named `Seiken Densetsu 3 (Japan) [En by LNF+Neill Corlett+SoM2Freak v1.01]`. This is covered by rule 3 and 4.
- The mere name `SEIKEN3` does not provide enough information to determine the language. Most likely it will be English. In any case, according to the above rule-set, the last rule will apply with English as fallback.

## UI Changes

When loading a save file, the program will automatically try to determine the used translation patch. In addition, you can also select the translation patch manually from the combo box at the top.

If you change the translation patch after having loaded a save file, the current player names will automatically be mapped to the new encoding, thus, leading to a possible drop of unsupported characters. If this happens, just load the save file again.

Also, the program will check for unsupported characters on input, which means you can only enter valid characters from the currently selected translation patch. Although, most ASCII characters are present in all language encodings.

For compatibility both half-width and full-width characters are supported.

A player's name is limited to a maximum length of 6 characters.

## Remarks

There are currently two encoding files to choose from when converting from Japanese to Unicode: One with full-width encoding in Unicode and the other one with half-width encoding in Unicode. Both work equally well. For now I went with full-width.

You can change this by simply overwriting `encoding_japanese_to_unicode.json` with either `encoding_japanese_to_unicode_halfwidth.json` or `encoding_japanese_to_unicode_fullwidth.json`.

Despite, when converting from Unicode to Japanese, both half-width and full-width characters are supported regardlessly.

## Known Issues

- The Italian and the Spanish cartridge encoding both have a codepoint for the double L (ll). However, there is no according Unicode codepoint for it.

