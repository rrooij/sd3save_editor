from sd3save_editor import checksum

header_end = 0x70  # End of the save header and start of save
save_end = 0x7FD
save_distance = 0x800  # Distance between seiken 3 save entries
location_offset = 0x726  # Player's location
checksum_offset = 0x7FE  # Place where checksum is stored
luc_offset = 0x491  # Luc, amount of money, 3 bytes
character_1_header_name_offset = 0x10
character_1_name_offset = 0x46d


def read_save(filepath):
    f = open(filepath, 'r+b')
    if not check_valid_save(f):
        raise Exception("Not a valid Seiken 3 save")
    return f


def check_valid_save(save):
    entries = read_available_entries(save)
    if not all(entries):
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

    save.seek(calculate_offset(character_1_name_offset, index))

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
    save.seek(calculate_offset(luc_offset, index))
    luc = int.from_bytes(save.read(3), byteorder='little')
    return luc


def write_luc(save, luc, index=0):
    """Write certain amount of luc"""
    save.seek(calculate_offset(luc_offset, index))
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
        offset = calculate_offset(character_1_header_name_offset,
                                  index) + (space_between * idx)
        save.seek(offset)
        save.write(encoded)
        save.write(zeroes)
        save.seek(calculate_offset(character_1_name_offset) + (12 * idx))
        save.write(encoded)
        save.write(zeroes)


def calculate_checksum(save, index=0):
    """Calculate 16 bit checksum for Seiken 3 Save

    Keyword arguments:
    save -- Seiken Densetsu 3 Save File opened in binary mode
    """
    current_header_end = calculate_offset(header_end, index=index)
    save.seek(current_header_end)
    data = save.read(save_end - header_end + 1)
    return checksum.sum16_checksum(data)


def write_checksum(save, index=0):
    """Write 16 bit checksum to Seiken 3 Save

    Keyword arguments:
    save -- Seiken Densetsu 3 Save File opened in binary mode
    index -- Save number to use
    """
    checksum = calculate_checksum(save, index)
    write_16bit_int(save, checksum_offset, checksum, index=index)


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
    write_16bit_int(save, location_offset, location_id, endian='little')


def read_location(save, index=0):
    """ Read the player's location """
    save.seek(location_offset)
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
    return offset + (save_distance * index)


def close_save(save):
    write_checksum(save)
    save.close()


class NameTooLongException(Exception):
    pass
