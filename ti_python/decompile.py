import pathlib
from .encoder import tokens

def decompile(file: pathlib.Path, output: pathlib.Path):
    with open(file, "rb") as o:
        header = o.read(55 + 19)
        
        keys = tokens.tokens.keys()
        vals = tokens.tokens.values()
        prev = None
        for token in o.read(file.stat().st_size - o.tell() - 2):
            try:
                if prev:
                    l = list(vals).index(prev.to_bytes() + token.to_bytes())
                    prev = None
                else:
                    l = list(vals).index(token.to_bytes())
            except:
                if prev:
                    print("\nunknown: ", token.to_bytes())
                prev = token
                continue
            print(list(keys)[l].replace("\\n", "\n"), end="", file=open(output, "a"))