import json
import os.path


def parse_json_game_data(filename) -> dict:
    script_dir = os.path.dirname(__file__)
    json_data = open(os.path.join(script_dir, 'data/' + filename))
    json_loaded = json.load(json_data)
    return json_loaded


def parse_locations_json() -> dict:
    return parse_json_game_data('locations.json')


def parse_storage_json() -> dict:
    return parse_json_game_data('item_storage.json')


def print_locations(locations):
    for location in locations:
        print(location)


def parse_tracks_json() -> dict:
    return parse_json_game_data('tracks.json')


def parse_encoding_english_to_unicode_json() -> dict:
    return parse_json_game_data('encoding_english_to_unicode.json')


def parse_encoding_french_to_unicode_json() -> dict:
    return parse_json_game_data('encoding_french_to_unicode.json')


def parse_encoding_german_to_unicode_json() -> dict:
    return parse_json_game_data('encoding_german_to_unicode.json')


def parse_encoding_italian_to_unicode_json() -> dict:
    return parse_json_game_data('encoding_italian_to_unicode.json')


def parse_encoding_japanese_to_unicode_json() -> dict:
    return parse_json_game_data('encoding_japanese_to_unicode.json')


def parse_encoding_spanish_to_unicode_json() -> dict:
    return parse_json_game_data('encoding_spanish_to_unicode.json')


def parse_encoding_unicode_to_english_json() -> dict:
    return parse_json_game_data('encoding_unicode_to_english.json')


def parse_encoding_unicode_to_french_json() -> dict:
    return parse_json_game_data('encoding_unicode_to_french.json')


def parse_encoding_unicode_to_german_json() -> dict:
    return parse_json_game_data('encoding_unicode_to_german.json')


def parse_encoding_unicode_to_italian_json() -> dict:
    return parse_json_game_data('encoding_unicode_to_italian.json')


def parse_encoding_unicode_to_japanese_json() -> dict:
    return parse_json_game_data('encoding_unicode_to_japanese.json')


def parse_encoding_unicode_to_spanish_json() -> dict:
    return parse_json_game_data('encoding_unicode_to_spanish.json')
