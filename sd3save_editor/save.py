from sd3save_editor import checksum
from datetime import timedelta

HEADER_END = 0x70  # End of the save header and start of save
SAVE_END = 0x7FD
SAVE_DISTANCE = 0x800  # Distance between seiken 3 save entries
LOCATION_OFFSET = 0x726  # Player's location
CHECKSUM_OFFSET = 0x7FE  # Place where checksum is stored
LUC_OFFSET = 0x491  # Luc, amount of money, 3 bytes
CHARACTER_1_HEADER_NAME_OFFSET = 0x10
CHARACTER_1_NAME_OFFSET = 0x46d
CHARACTER_1_CURRENT_HP = 0x172
CHARACTER_1_MAX_HP = 0x1FD
CURRENT_MUSIC = 0x2C
TIME_OFFSET = 0x6C


def read_save(filepath):
    f = open(filepath, 'r+b')
    if not check_valid_save(f):
        raise Exception("Not a valid Seiken 3 save")
    return f


def check_valid_save(save):
    """Check if the save is valid. Not very reliable, but
       the least I can do for now to prevent people from
       messing up files"""
    entries = read_available_entries(save)
    if not entries[0] and not entries[1] and not entries[2]:
        return False
    return True


def read_available_entries(save):
    """Return which indexes are available"""
    has_first = True if check_entry_exists(save, 0) else False
    has_second = True if check_entry_exists(save, 1) else False
    has_third = True if check_entry_exists(save, 2) else False
    return (has_first, has_second, has_third)


def check_entry_exists(save, index=0):
    """Check if save entry exists"""
    save.seek(calculate_offset(0, index))
    text = save.read(5)
    if text == b'exist':
        return True
    return False


def read_time(save, index=0):
    save.seek(TIME_OFFSET)
    seconds = int.from_bytes(save.read(4), byteorder='little') / 60
    return timedelta(seconds=seconds)


def write_time(save, timedelta, index=0):
    save.seek(TIME_OFFSET)
    seconds = int(timedelta.total_seconds()) * 60
    save.write(seconds.to_bytes(4, byteorder='little'))


def read_current_music(save, index=0):
    """Read the music being played"""
    save.seek(CURRENT_MUSIC)
    return int.from_bytes(save.read(1), byteorder='little')


def write_current_music(save, music_id, index=0):
    """Write current music to be played"""
    save.seek(CURRENT_MUSIC)
    save.write(music_id.to_bytes(1, byteorder='little'))


def read_current_hp(save, index=0, character_index=0):
    """Read current HP of character"""
    save.seek(calculate_char_stat_offset(CHARACTER_1_CURRENT_HP,
                                         index,
                                         character_index))
    return int.from_bytes(save.read(2), byteorder='little')


def write_current_hp(save, hp, index=0, character_index=0):
    """Write current HP of character"""
    save.seek(calculate_char_stat_offset(CHARACTER_1_CURRENT_HP,
                                         index,
                                         character_index))
    save.write(hp.to_bytes(2, byteorder='little'))


def read_max_hp(save, index=0, character_index=0):
    """Read max. HP of character"""
    save.seek(calculate_char_stat_offset(CHARACTER_1_MAX_HP,
                                         index,
                                         character_index))
    return int.from_bytes(save.read(2), byteorder='little')


def write_max_hp(save, hp, index=0, character_index=0):
    """Write max. HP of character"""
    save.seek(calculate_char_stat_offset(CHARACTER_1_MAX_HP,
                                         index,
                                         character_index))
    save.write(hp.to_bytes(2, byteorder='little'))


def calculate_char_stat_offset(offset, index=0, character_index=0):
    char_difference = 0xff
    return calculate_offset(offset,
                            index) + (character_index *
                                      char_difference)


def read_character_names(save, index=0):
    """Read names of the main 3 characters"""

    save.seek(calculate_offset(CHARACTER_1_NAME_OFFSET, index))

    first_character = decode_char_string(save.read(12))
    second_character = decode_char_string(save.read(12))
    third_character = decode_char_string(save.read(12))

    return (first_character, second_character, third_character)


def decode_char_string(char_name):
    """Decode character name and strip zeroes"""
    replace_char = '\x00'
    return char_name.decode('utf-16-le', 'backslashreplace') \
                    .rstrip(replace_char)


def read_luc(save, index=0):
    """ Read amount of luc"""
    save.seek(calculate_offset(LUC_OFFSET, index))
    luc = int.from_bytes(save.read(3), byteorder='little')
    return luc


def write_luc(save, luc, index=0):
    """Write certain amount of luc"""
    save.seek(calculate_offset(LUC_OFFSET, index))
    converted = luc.to_bytes(3, byteorder='little')
    save.write(converted)


def change_character_names(save, names, index=0):
    """Change player names
    """
    space_between = 0x20  # Each name in header is seperated by 0x20
    for idx, name in enumerate(names):
        if len(name) > 6:
            raise NameTooLongException("Name: {0} is too long. Max is 6"
                                       "characters".format(name))
        encoded = name.encode('utf-16-le')
        zeroes = bytearray(7 - len(name))
        offset = calculate_offset(CHARACTER_1_HEADER_NAME_OFFSET,
                                  index) + (space_between * idx)
        save.seek(offset)
        save.write(encoded)
        save.write(zeroes)
        save.seek(calculate_offset(CHARACTER_1_NAME_OFFSET) + (12 * idx))
        save.write(encoded)
        save.write(zeroes)


def calculate_checksum(save, index=0):
    """Calculate 16 bit checksum for Seiken 3 Save

    Keyword arguments:
    save -- Seiken Densetsu 3 Save File opened in binary mode
    """
    current_header_end = calculate_offset(HEADER_END, index=index)
    save.seek(current_header_end)
    data = save.read(SAVE_END - HEADER_END + 1)
    return checksum.sum16_checksum(data)


def write_checksum(save, index=0):
    """Write 16 bit checksum to Seiken 3 Save

    Keyword arguments:
    save -- Seiken Densetsu 3 Save File opened in binary mode
    index -- Save number to use
    """
    checksum = calculate_checksum(save, index)
    write_16bit_int(save, CHECKSUM_OFFSET, checksum, index=index)


def write_all_checksums(save, indexes):
    """Write all checksums vor valid saves"""
    for number, is_valid in enumerate(indexes):
        if is_valid:
            write_checksum(save, number)


def change_location(save, location_id, index=0):
    """Change player location and write it to save

    Keyword arguments:
    save -- Seiken Densetsu 3 Save File opened in binary mode
    location_id: Number of location to go to
    """
    write_16bit_int(save, LOCATION_OFFSET, location_id, endian='little')


def read_location(save, index=0):
    """ Read the player's location """
    save.seek(LOCATION_OFFSET)
    return int.from_bytes(save.read(2), byteorder='little')


def write_16bit_int(save, offset, integer, endian='big', index=0):
    """Write a 16 bit integer to Seiken Densetsu 3 save

    Keyword arguments:
    save -- Seiken Densetsu 3 Save File opened in binary mode
    offset -- Location to store the integer
    integer -- The integer to convert to 16 bit byte in Big Endian
    endian -- Byte order
    """
    save.seek(calculate_offset(offset, index))
    save.write((integer).to_bytes(2, byteorder=endian))


def calculate_offset(offset, index=0):
    return offset + (SAVE_DISTANCE * index)


def close_save(save):
    write_checksum(save)
    save.close()


class NameTooLongException(Exception):
    pass
