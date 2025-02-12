import pathlib
import argparse

from . import tokenizer, compiler

parser = argparse.ArgumentParser()

parser.add_argument('input', type=str, help="Path to input Python file")
parser.add_argument('--output', type=str, help="Output TI-BASIC file", required=False, default=None)

if __name__ == "__main__":
    args = parser.parse_args()

    input_file = pathlib.Path(args.input)

    if not input_file.exists():
        raise FileNotFoundError(f"Could not find input file {input_file.absolute()}")
    
    tree = tokenizer.parse(input_file.read_text())
    
    output_path = pathlib.Path(args.output if args.output else input_file.name.removesuffix('.py') + '.8xp')
    
    output_path.write_text(compiler.compile(tree))

    print("Compiled and written to", output_path.absolute())