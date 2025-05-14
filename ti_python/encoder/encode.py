"Encode TI-BASIC into 8XP files"

from tokens import tokens

SIGNATURE = b"**TI83F*\x1a\x0a"
COMMENT = b"Created by TI Python"
COMMENT += b"\x00" * (42 - len(COMMENT))

HEADER = SIGNATURE + b"\x0a" + COMMENT


def encode(src):
    global HEADER
    encoded = b""

    token = src

    while src:
        if len(token) > 1:
            token = token[:-1]

        # Check if valid
        if "".join(token) in tokens:
            encoded += tokens[token]

            src = src[len(token):] 
            token = src

    checksum = b"\x00\x00"

    # Metadata
    FLAG = b"\x0d"
    body_and_checksum_length = len(encoded + checksum).to_bytes(2, "little")
    PROGRAM_TYPE = b"\x05"

    PROGRAM_NAME = b"PROG1"
    PROGRAM_NAME += b"\x00" * (8 - len(PROGRAM_NAME))
    
    VERSION = b"\x00"
    ARCHIVED = b"\x00"

    body_and_checksum_length_2 = body_and_checksum_length
    body_length = len(encoded).to_bytes(2, "little")
    
    METADATA = FLAG + b"\x00" + body_and_checksum_length + PROGRAM_TYPE + PROGRAM_NAME + VERSION + ARCHIVED + body_and_checksum_length_2 + body_length
    print(len(METADATA))
    meta_and_body_length = len(METADATA + encoded).to_bytes(2, "little")

    HEADER += meta_and_body_length

    encoded = HEADER + METADATA + encoded + checksum
    return encoded

encode("Disp \"Hello\"")