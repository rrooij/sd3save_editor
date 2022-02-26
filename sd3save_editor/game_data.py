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
