def sum16_checksum(bytes, big=True):
    sum = 0
    count_to = len(bytes)
    count = 0

    while count_to > count:
        value = bytes[count + 1] + bytes[count]
        sum = sum + value
        count = count + 2

    if big:
        sum = sum >> 8 | (sum << 8 & 0xff00)  # Swap bytes for big endian
    return sum
