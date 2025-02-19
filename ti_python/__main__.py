import pathlib
import argparse

from . import tokenizer, compiler
from . import compile

parser = argparse.ArgumentParser(
    prog="ti-python",
    description="Compile Python code to TI-BASIC code",
    epilog="Made by @simplyrohan",
    usage="%(prog)s [-o output.txt] input.py",
)

parser.add_argument("input", type=str, help="Path to input Python file")
parser.add_argument(
    "-o",
    "--output",
    type=str,
    help="Output TI-BASIC file",
    required=False,
    default=None,
)


def main():
    args = parser.parse_args()

    input_file = pathlib.Path(args.input)

    if not input_file.exists():
        raise FileNotFoundError(f"Could not find input file {input_file.absolute()}")

    output_path = pathlib.Path(
        args.output if args.output else input_file.name.removesuffix(".py") + ".txt"
    )

    output_path.write_text(compile(input_file.read_text()))

    print("Compiled and written to", output_path.absolute())

if __name__ == "__main__":
    main()
