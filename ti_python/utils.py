import typing

COLOR_TEXT = lambda r, g, b: f"\u001b[38;2;{r};{g};{b}m"
BOLD = "\u001b[1m"
CLEAR = "\u001b[0m"

file_name = None

def log(msg: str, color: typing.Literal['green', 'none'] = 'none', bold=False, end="\n"):
    print(f"{BOLD if bold else ''}{COLOR_TEXT(120, 255, 120) if color == 'green' else ''}{msg}{CLEAR}", end=end)

def error(msg: str, line=None):
    r, g, b = 255, 120, 120
    location = ""

    if line != None:
        location = f"{file_name}:{line + 1}:"
    print(f"{BOLD}{location} {COLOR_TEXT(r, g, b)}error: {CLEAR}{BOLD}{msg}{CLEAR}")
    exit(1)
