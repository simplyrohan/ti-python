"""
Creates TI-BASIC commands through functions
"""
from .globals import *

def call_func(name: str, args: list[Type] = None):
    arguments = []

    if args:
        for arg in args:
            if type(arg) == Str:
                arguments.append(f'"{arg}"')
            elif type(arg) == Number:
                arguments.append(str(arg))
            elif type(arg) == Var:
                arguments.append(arg.value)
    return f":{name} {" ".join(arguments)}"

def store_var(name: Var, value: Type):
    return f":{value.value}→{name.value.upper()}"