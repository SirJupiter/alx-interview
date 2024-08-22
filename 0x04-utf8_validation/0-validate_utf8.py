#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set repreents a valid UTF-8 encoding

    Args:
        data (any) - data set to be checked

    Returns:
        True if data is a valid UTF-8 encoding
        False if otherwise
    """
    num_of_bytes = 0

    for byte in data:
        byte = byte & 0xFF

        if num_of_bytes == 0:
            if (byte >> 7) == 0b0:  # 0xxxxxxx - 1 byte
                continue
            elif (byte >> 5) == 0b110:  # 110xxxxx - 2 bytes
                num_of_bytes = 1
            elif (byte >> 4) == 0b1110:  # 1110xxxx - 3 bytes
                num_of_bytes = 2
            elif (byte >> 3) == 0b11110:  # 11110xxx - 4 bytes
                num_of_bytes = 3
            else:  # Not a valid starting byte
                return False
        else:  # We are expecting continuation bytes
            if (byte >> 6) != 0b10:  # 10xxxxxx
                return False
            num_of_bytes -= 1

    # If we finish processing and expect no more bytes
    return num_of_bytes == 0
