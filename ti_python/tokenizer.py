# I am aware this is redundant, but I may try bootstrapping the tokenizer in the future
import ast


def parse(code):
    return ast.parse(code)
