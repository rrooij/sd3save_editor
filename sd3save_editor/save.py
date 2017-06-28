from sd3save_editor import checksum, game_data
from construct import (Adapter, Byte, Bytes, Checksum, Const, Struct,
                       Int8sl, Int16sl, Int16ub, Int16ul, Int32sl,
                       Sequence, this, RawCopy, Optional)


class TimeAdapter(Adapter):
    """Convert seconds to seiken densetsu 3 time
       Time is saved as a 60th of a second
    """
    def _decode(self, obj, context):
        return int(obj / 60)

    def _encode(self, obj, context):
        return int(obj * 60)


class CharacterNameAdapter(Adapter):
    """Convert name to utf16-le
       The maximum length of the character set is 8F

       The character encoding is latin subset utf-16-le with
       some added symbols in the 8X range.

       TODO: Find out Japanese character encoding
    """

    SPECIAL_CHARACTERS = {
        "heart": {
            "utf16": b'\x64\x27',
            "seiken3": b'\x8d\x00'
        },
        "right_arrow": {
            "utf16": b'\xa1\x27',
            "seiken3": b'\x8b\x00'
        },
        "left_arrow": {
            "utf16": b'\x05\x2b',
            "seiken3": b'\x8a\x00'
        },
        "up_arrow": {
            "utf16": b'\x91\x21',
            "seiken3": b'\x88\x00'
        },
        "down_arrow": {
            "utf16": b'\x93\x21',
            "seiken3": b'\x89\x00'
        },
        "˼": {
            "utf16": b'\xfc\x02',
            "seiken3": b'\x82\x00',
        },
        "circle": {
            "utf16": b'\xcb\x25',
            "seiken3": b'\x83\x00'
        },
        "circle_filled": {
            "utf16": b'\xcf\x25',
            "seiken3": b'\x84\x00'
        },
        "circle_filled_small": {
            "utf16": b'\xcf\x25',
            "seiken3": b'\x84\x00'
        },
        "small_x": {
            "utf16": b'\x93\x20',
            "seiken3": b'\x85\x00'
        },
        "˹": {
            "utf16": b'\xf9\x02',
            "seiken3": b'\x87\x00'
        },
        "..": {
            "utf16": b'\x25\x20',
            "seiken3": b'\x86\x00'
        },
        "down_triangle": {
            "utf16": b'\xbe\x25',
            "seiken3": b'\x8b\x00'
        }
    }

    def _decode(self, obj, context):
        replace_char = '\x00'
        for key, character in self.SPECIAL_CHARACTERS.items():
            obj = obj.replace(character['seiken3'], character['utf16'])
        return obj.decode('utf-16-le',
                          'backslashreplace').rstrip(replace_char)

    def _encode(self, obj, context):
        zeroes = bytearray(12)
        name = obj.encode('utf-16-le')
        for key, character in self.SPECIAL_CHARACTERS.items():
            name = name.replace(character['utf16'], character['seiken3'])
        for idx, char in enumerate(name):
            zeroes[idx] = char
        return zeroes


char_header = Struct(
    "name"/CharacterNameAdapter(Bytes(12)),
    "lvl"/Int8sl,
    "current_hp"/Int16sl,
    "max_hp"/Int16sl,
    "current_mp"/Int16sl,
    "max_mp"/Int16sl,
    "unclear"/Bytes(7)
)

save_header = Struct(
    "exist_string"/Const(b"exist   "),
    "unclear"/Bytes(8),
    "char1"/char_header,
    "playing_music"/Int8sl,
    "unclear2"/Bytes(3),
    "char2"/char_header,
    "location_name"/Int8sl,
    "unclear3"/Bytes(3),
    "char3"/char_header,
    "time_played"/TimeAdapter(Int32sl)
)

character_stats = Struct(
    "current_hp"/Int16sl,
    "current_mp"/Int16sl,
    "strength"/Int8sl,
    "agility"/Int8sl,
    "vitality"/Int8sl,
    "int"/Int8sl,
    "spirit"/Int8sl,
    "luck"/Int8sl,
    "total_exp"/Int16sl,
    "remainder_total_exp"/Int16sl,
    "unclear"/Bytes(5),
    "tech_gauge_max"/Int8sl,
    "exp_for_next_level"/Int16sl,
    "remainder_exp_next_level"/Int16sl,
    "lvl"/Int8sl,
    "unclear2"/Byte,
    "character_skin"/Int8sl,
    "class_change_made"/Int8sl,
    "class"/Int8sl,
    "equipped_weapon"/Int8sl,
    "equipped_helmet"/Int8sl,
    "equipped_armor"/Int8sl,
    "equipped_gauntlet"/Int8sl,
    "equipped_shield"/Int8sl,
    "unclear3"/Bytes(19),  # Not known yet :(
    "attack_power"/Int16sl,
    "unclear4"/Bytes(5),  # Also unkown
    "evade_rate"/Int8sl,
    "defense_power"/Int16sl,
    "magic_defense_power"/Int16sl,
    "unkown_could_be_power"/Int16sl,
    "extra_weapons"/Int8sl[7],
    "unclear5"/Bytes(9),
    "extra_armor"/Int8sl[7],  # TODO: Do something with extra equipment
    "unclear6"/Bytes(9),  # Unknown,
    "extra_gauntlets"/Int8sl[7],
    "unclear7"/Byte,  # Unknown
    "extra_shields"/Int8sl[7],
    "unclear8"/Byte,  # Unkown
    "spells"/Int8sl[12],
    "targeting_values"/Int8sl[12],
    "max_hp"/Int16sl,
    "max_mp"/Int16sl
)

save_data = Struct(
    "still_unknown"/Bytes(258),
    "char1"/character_stats,
    "unclear"/Bytes(112),
    "char2"/character_stats,
    "unclear2"/Bytes(112),
    "char3"/character_stats,
    "unclear3"/Bytes(110),
    "character_names"/CharacterNameAdapter(Bytes(12))[3],
    "luc"/Int16ul,
    "unclear4"/Bytes(529),
    "item_storage"/Int8sl[103],
    "unclear5"/Bytes(27),
    "location"/Int16sl,
    "unclear6"/Bytes(46),
    "item_ring"/Int8sl[10],
    "unclear7"/Bytes(158)
)

save_entry = Struct(
    "header"/save_header,
    "data"/RawCopy(save_data),
    "checksum"/Checksum(Int16ub,
                        lambda data: checksum.sum16_checksum(data),
                        this.data.data)
)


save_format = Sequence(
    Optional(save_entry),
    Optional(save_entry),
    Optional(save_entry)
)


def read_save(filepath):
    f = open(filepath, 'r+b')
    save_data = save_format.parse(f.read())
    if not check_valid_save(save_data):
        raise Exception("Not a valid Seiken 3 save")
    return save_data


def write_save(filepath, data):
    for entry in data:
        if entry and "data" in entry.data:
            del entry.data.data
    open(filepath, 'wb').write(save_format.build(data))


def write_save_stream(stream, data):
    for entry in data:
        if "data" in entry.data:
            del entry.data.data
    stream.seek(0)
    stream.write(save_format.build(data))


def check_valid_save(save_data):
    """Check if the save is valid. Not very reliable, but
       the least I can do for now to prevent people from
       messing up files"""
    if not save_data[0] and not save_data[1] and not save_data[2]:
        return False
    return True


def write_character_names(save_data, character_names, index=0):
    """Write character names to save data"""
    save_data[index].data.value.character_names = character_names
    save_data[index].header.char1.name = character_names[0]
    save_data[index].header.char2.name = character_names[1]
    save_data[index].header.char2.name = character_names[2]


def write_storage_item_amounts(save_data, items, index=0):
    """Write amount of multiple items.

    Keyword arguments:
    save -- Save file opened in binary mode
    items -- Dictionairy with index of item and amount
    index -- Save entry number
    """
    for item_index, amount in items.items():
        save_data[index].data.value.item_storage[item_index] = amount


def read_all_storage_items_amount(save_data, index=0):
    item_names = game_data.parse_storage_json()
    items = []
    for idx, item_name in enumerate(item_names):
        amount = save_data[index].data.value.item_storage[idx]
        if amount > 99:
            raise AmountTooBigException("Amount should be lower than 100")
        items.append((item_name, amount))
    return items


class NameTooLongException(Exception):
    pass


class AmountTooBigException(Exception):
    pass
