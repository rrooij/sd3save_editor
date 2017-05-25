from sd3save_editor import checksum

header_end = 0x70  # End of the save header and start of save
save_end = 0x7FD
location_offset = 0x726  # Player's location
checksum_offset = 0x7FE  # Place where checksum is stored


def read_save(filepath):
    f = open(filepath, 'r+b')
    return f

def check_valid_save(save):
    """Check if the save is valid. Not very reliable, but
       the least I can do for now to prevent people from
       messing up files"""
    save.seek(0)
    text = save.read(5)
    if text == b'exist':
        return True
    return False

def calculate_checksum(save):
    """Calculate 32 bit checksum for Seiken 3 Save

    Keyword arguments:
    save -- Seiken Densetsu 3 Save File opened in binary mode
    """
    save.seek(header_end)
    data = save.read(save_end - header_end + 1)
    return checksum.sum16_checksum(data)

def write_checksum(save):
    """Write 32 bit checksum to Seiken 3 Save

    Keyword arguments:
    save -- Seiken Densetsu 3 Save File opened in binary mode
    """
    checksum = calculate_checksum(save)
    write_16bit_int(save, checksum_offset, checksum)


def change_location(save, location_id):
    """Change player location and write it to save

    Keyword arguments:
    save -- Seiken Densetsu 3 Save File opened in binary mode
    location_id: Number of location to go to
    """
    save.seek(location_offset)
    write_16bit_int(save, location_offset, location_id)


def write_16bit_int(save, offset, integer):
    """Write a 16 bit integer to Seiken Densetsu 3 save in 16 bit Big Endian

    Keyword arguments:
    save -- Seiken Densetsu 3 Save File opened in binary mode
    offset -- Location to store the integer
    integer -- The integer to convert to 16 bit byte in Big Endian
    """
    save.seek(offset)
    save.write((integer).to_bytes(2, byteorder='big'))


def close_save(save):
    write_checksum(save)
    save.close()
