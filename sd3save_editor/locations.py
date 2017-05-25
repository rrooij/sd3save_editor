import json
import os.path

locations = []

def parse_locations_json():
    global locations # Global is just for caching, sorry
    script_dir = os.path.dirname(__file__)
    json_data = open(os.path.join(script_dir, 'data/locations.json'))
    locations = json.load(json_data)
    return locations

def get_locations():
    if not locations:
        parse_locations_json()
    return locations

def print_locations(locations):
    for location in locations:
        print(location)
