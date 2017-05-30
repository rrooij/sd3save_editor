from sd3save_editor import checksum

HEADER_END = 0x70  # End of the save header and start of save
SAVE_END = 0x7FD
SAVE_DISTANCE = 0x800  # Distance between seiken 3 save entries
LOCATION_OFFSET = 0x726  # Player's location
CHECKSUM_OFFSET = 0x7FE  # Place where checksum is stored
LUC_OFFSET = 0x491  # Luc, amount of money, 3 bytes
CHARACTER_1_HEADER_NAME_OFFSET = 0x10
CHARACTER_1_NAME_OFFSET = 0x46d


def read_save(filepath):
    f = open(filepath, 'r+b')
    if not check_valid_save(f):
        raise Exception("Not a valid Seiken 3 save")
    return f


def check_valid_save(save):
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
    """Check if the save is valid. Not very reliable, but
       the least I can do for now to prevent people from
       messing up files"""
    save.seek(calculate_offset(0, index))
    text = save.read(5)
    if text == b'exist':
        return True
    return False


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
    """Write a 16 bit integer to Seiken Densetsu 3 save in 16 bit

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
