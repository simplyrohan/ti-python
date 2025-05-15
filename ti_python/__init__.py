from .compiler import compile_tree
from .tokenizer import parse
from . import utils
from .encoder.decompile import decompile

def compile(code: str, filename: str=None):
    utils.file_name = filename or "<unknown>"
    return compile_tree(parse(code))
