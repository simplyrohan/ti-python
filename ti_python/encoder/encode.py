"Encode TI-BASIC into 8XP files"

from .tokens import tokens


def encode(src):
    encoded = b""

    src = list(src) + [" "]

    token = ""

    while src:
        while token in [tok[: len(token)] for tok in tokens]:
            token += src.pop(0)
        if token[:-1] not in tokens:
            raise SyntaxError(f"Unknown token '{token[:-1]}'")
        encoded += tokens[token[:-1]]
        token = token[-1]

    return encoded
