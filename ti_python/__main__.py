import pathlib
import argparse

from . import compile
from . import utils
from .encoder.decompile import decompile
from .encoder.encode import encode


class ArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        utils.error(message)


parser = ArgumentParser(
    prog="ti-python",
    description="Compile Python code to TI-BASIC code",
    epilog="Made by @simplyrohan",
    usage="%(prog)s [-o output.8xp/txt] input.py",
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
    "--decompile",
    type=str,
    metavar="",
    help="decompile an 8XP file to it's TI-BASIC source",
    required=False,
    default=None,
)
parser.add_argument(
    "--compile",
    type=str,
    metavar="",
    help="compile an TI-BASIC program to an 8XP file",
    required=False,
    default=None,
)

def main():
    args = parser.parse_args()


    # ti-basic compiler
    if args.compile:
        input_file = pathlib.Path(args.compile)

        if not input_file.exists():
            utils.error(f"could not find input file {input_file.absolute()}")

        output_path = pathlib.Path(
            args.output
            if args.output
            else input_file.name.removesuffix(".txt") + ".8xp"
        )
        # output_path.write_text("")
        output_path.write_bytes(encode(input_file.read_text()))
        print("Compiled and written to", output_path.absolute())
        return
    # decompiler
    if args.decompile:
        input_file = pathlib.Path(args.decompile)

        if not input_file.exists():
            utils.error(f"could not find input file {input_file.absolute()}")

        output_path = pathlib.Path(
            args.output
            if args.output
            else input_file.name.removesuffix(".8xp") + ".txt"
        )
        output_path.write_text("")
        decompile(input_file, output_path)
        print("Decompiled and written to", output_path.absolute())
        return
    
    # argument validation
    if len(args.input) == 0:
        utils.error("no input files")

    input_file = pathlib.Path(args.input[0])

    if not input_file.exists():
        utils.error(f"could not find input file {input_file.absolute()}")

    output_path = pathlib.Path(
        args.output if args.output else input_file.name.removesuffix(".py") + ".8xp"
    )

    # compile
    compiled = compile(input_file.read_text(), input_file.absolute())

    utils.log(f"Writing to ", end="")
    utils.log(output_path.absolute(), bold=True)
    if str(output_path).lower().endswith('.8xp'): # 8xp output
        output_path.write_bytes(encode(compiled))
    else: # TI-BASIC output
        output_path.write_text(compiled)

    # print("Done!")
    utils.log("Done!", 'green', True)


if __name__ == "__main__":
    main()
