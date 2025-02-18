from .compiler import compile_tree
from .tokenizer import parse


def compile(code: str):
    return compile_tree(parse(code))
