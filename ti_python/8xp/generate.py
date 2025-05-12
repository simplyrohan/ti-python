# Generate tokens.py from tokens.xml
import xml
import pathlib
import xml.etree.ElementTree as ElementTree

dir = pathlib.Path(__file__).parent
tokensXML = ElementTree.parse(dir / "tokens.xml").getroot()

tokensList = tokensXML.findall("{http://merthsoft.com/Tokens}Token")

py = "tokens = {"


def generateTokens(tokens, byte_prefix=""):
    out = ""
    for token in tokens:
        string = token.get("string")
        if string:
            string = string.replace("\\", "\\\\")
            string = string.replace('"', '\\"')

            byte = byte_prefix + token.get("byte").replace("$", "\\x")
            out += f'"{string}": b"{byte}"' + ",\n    "

        if token.get("stringTerminator") == "false":
            out += generateTokens(
                token.findall("{http://merthsoft.com/Tokens}Token"),
                byte_prefix + token.get("byte").replace("$", "\\x"),
            )
    return out


py += generateTokens(tokensList)
py += "}\n"

with open(dir / "tokens.py", "w") as tokensPy:
    tokensPy.write(py)
