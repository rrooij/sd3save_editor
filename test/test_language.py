import os
import pytest

from sd3save_editor.gui.mainwindow import MainWindow
from sd3save_editor.save import Language


def test_detect_language_from_filename():
    assert MainWindow.detectLanguage("") == Language.ENGLISH # fallback
    assert MainWindow.detectLanguage("Something") == Language.ENGLISH # fallback
    assert MainWindow.detectLanguage("SEIKEN3") == Language.ENGLISH # fallback
    assert MainWindow.detectLanguage("SD3EN101") == Language.ENGLISH
    assert MainWindow.detectLanguage("SEIKEN3F") == Language.FRENCH
    assert MainWindow.detectLanguage("SEIKEN3D") == Language.GERMAN
    assert MainWindow.detectLanguage("SD3GER203") == Language.GERMAN
    assert MainWindow.detectLanguage("SD3DE30") == Language.GERMAN
    assert MainWindow.detectLanguage("SD3_JAP_ITA_V100_BETA_6A93E9F") == Language.ITALIAN
    assert MainWindow.detectLanguage("SD3_ENG_ITA_V100_BETA_6A93E9F") == Language.ITALIAN
    assert MainWindow.detectLanguage("SOM2SP") == Language.SPANISH
    assert MainWindow.detectLanguage("Seiken Densetsu 3 (J)") == Language.JAPANESE
    assert MainWindow.detectLanguage("Seiken Densetsu 3 (Japan)") == Language.JAPANESE
    assert MainWindow.detectLanguage("Seiken Densetsu 3 (Japan) [En by LNF+Neill Corlett+SoM2Freak v1.01]") == Language.ENGLISH
    assert MainWindow.detectLanguage("english") == Language.ENGLISH
    assert MainWindow.detectLanguage("french") == Language.FRENCH
    assert MainWindow.detectLanguage("français") == Language.FRENCH
    assert MainWindow.detectLanguage("francais") == Language.FRENCH
    assert MainWindow.detectLanguage("german") == Language.GERMAN
    assert MainWindow.detectLanguage("deutsch") == Language.GERMAN
    assert MainWindow.detectLanguage("italian") == Language.ITALIAN
    assert MainWindow.detectLanguage("italiano") == Language.ITALIAN
    assert MainWindow.detectLanguage("japanese") == Language.JAPANESE
    assert MainWindow.detectLanguage("spanish") == Language.SPANISH
    assert MainWindow.detectLanguage("español") == Language.SPANISH
    assert MainWindow.detectLanguage("espanol") == Language.SPANISH
    assert MainWindow.detectLanguage("castellano") == Language.SPANISH
    assert MainWindow.detectLanguage("ENGLISH") == Language.ENGLISH
    assert MainWindow.detectLanguage("FRENCH") == Language.FRENCH
    assert MainWindow.detectLanguage("FRANÇAIS") == Language.FRENCH
    assert MainWindow.detectLanguage("FRANCAIS") == Language.FRENCH
    assert MainWindow.detectLanguage("GERMAN") == Language.GERMAN
    assert MainWindow.detectLanguage("DEUTSCH") == Language.GERMAN
    assert MainWindow.detectLanguage("ITALIAN") == Language.ITALIAN
    assert MainWindow.detectLanguage("ITALIANO") == Language.ITALIAN
    assert MainWindow.detectLanguage("JAPANESE") == Language.JAPANESE
    assert MainWindow.detectLanguage("SPANISH") == Language.SPANISH
    assert MainWindow.detectLanguage("ESPAÑOL") == Language.SPANISH
    assert MainWindow.detectLanguage("ESPANOL") == Language.SPANISH
    assert MainWindow.detectLanguage("CASTELLANO") == Language.SPANISH
    assert MainWindow.detectLanguage("Something [EN]") == Language.ENGLISH
    assert MainWindow.detectLanguage("Something [FR]") == Language.FRENCH
    assert MainWindow.detectLanguage("Something [DE]") == Language.GERMAN
    assert MainWindow.detectLanguage("Something [IT]") == Language.ITALIAN
    assert MainWindow.detectLanguage("Something [JA]") == Language.JAPANESE
    assert MainWindow.detectLanguage("Something [JP]") == Language.JAPANESE
    assert MainWindow.detectLanguage("Something [ES]") == Language.SPANISH
    assert MainWindow.detectLanguage("Something [SP]") == Language.SPANISH
    assert MainWindow.detectLanguage("Something [ENG]") == Language.ENGLISH
    assert MainWindow.detectLanguage("Something [FRA]") == Language.FRENCH
    assert MainWindow.detectLanguage("Something [DEU]") == Language.GERMAN
    assert MainWindow.detectLanguage("Something [GER]") == Language.GERMAN
    assert MainWindow.detectLanguage("Something [ITA]") == Language.ITALIAN
    assert MainWindow.detectLanguage("Something [JAP]") == Language.JAPANESE
    assert MainWindow.detectLanguage("Something [ESP]") == Language.SPANISH
    assert MainWindow.detectLanguage("Something [SPA]") == Language.SPANISH

