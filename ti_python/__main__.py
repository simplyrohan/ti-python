import pathlib
import argparse

from . import compile
from .error import error
from .encoder.decompile import decompile


class ArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        error(message)


parser = ArgumentParser(
    prog="ti-python",
    description="Compile Python code to TI-BASIC code",
    epilog="Made by @simplyrohan",
    usage="%(prog)s [-o output.txt] input.py",
)


parser.add_argument("input", nargs="*", type=str, help="Path to input Python file")
parser.add_argument(
    "-o",
    "--output",
    type=str,
    metavar="",
    help="output TI-BASIC file",
    required=False,
    default=None,
)
parser.add_argument(
    "-d",
    "--decompile",
    type=str,
    metavar="",
    help="decompile an 8XP file to it's TI-BASIC source",
    required=False,
    default=None,
)


def main():
    args = parser.parse_args()

    # argument validation
    if args.decompile:
        input_file = pathlib.Path(args.decompile)

        if not input_file.exists():
            error(f"could not find input file {input_file.absolute()}")

        output_path = pathlib.Path(
            args.output
            if args.output
            else input_file.name.removesuffix(".8xp") + ".txt"
        )
        output_path.write_text("")
        decompile(input_file, output_path)
        print("Decompiled and written to", output_path.absolute())
        return

    elif len(args.input) == 0:
        error("no input files")

    input_file = pathlib.Path(args.input[0])

    if not input_file.exists():
        error(f"could not find input file {input_file.absolute()}")

    output_path = pathlib.Path(
        args.output if args.output else input_file.name.removesuffix(".py") + ".txt"
    )

    output_path.write_text(compile(input_file.read_text()))

    print("Compiled and written to", output_path.absolute())


if __name__ == "__main__":
    main()
