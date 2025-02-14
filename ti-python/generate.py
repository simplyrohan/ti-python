"""
Generates TI-BASIC commands from parameters
"""
from .globals import *

def _call_func(name, args: list[Type] = None):
    arguments = []

    if args:
        for arg in args:
            if type(arg) == Str:
                arguments.append(f'"{arg.value}"')
            elif type(arg) == Number:
                arguments.append(str(arg.value))
            elif type(arg) == Var:
                arguments.append(arg.value)
    return f"{name} {",".join(arguments)}"

def call_func(name: str, args: list[Type] = None):
    return f":{_call_func(name, args)}"

def store_var(name: Var, value: Type):
    if type(value) == Number:
        return f":{value.value}→{name.value.upper()}"
    elif type(value) == tuple:
        return f":{_call_func(value[0], value[1])}→{name.value.upper()}"
    elif type(value) == Var:
        return f":{value.value}→{name.value.upper()}"