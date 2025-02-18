"""
Generates TI-BASIC commands from parameters
"""

from . import types

def create_val(val):
    if type(val) == types.Number:
        return f"{val.value}"
    elif type(val) == types.Name:
        return f"{val.value.upper()}"
    elif type(val) == types.Call:
        return f"{call_func(val.value)}"
    elif type(val) == types.Str:
        return f"\"{val.value}\""
    elif issubclass(type(val), types.Op):
        match type(val):
            case types.Add:
                op = "+"
            case types.Sub:
                op = "-"
            case types.Mul:
                op = "*"
            case types.Div:
                op = "/"
        return f"{create_val(val.left)}{op}{create_val(val.right)}"


def call_func(call: types.Call):
    arguments = []

    if call.args:
        for arg in call.args:
            arguments.append(create_val(arg))
    return f"{call.value} {','.join(arguments)}"


def assign_val(assign: types.Assign):
    return create_val(assign.value) + f"→{assign.target.value.upper()}"


def create_block(block: types.Block):
    if issubclass(type(block), types.If):
        comp = ""
        match type(block.head):
            case types.LessThan:
                comp = "<"
            case types.GreaterThan:
                comp = ">"
            case types.EqualTo:
                comp = "="
            case types.NotEqualTo:
                comp = "≠"
            case types.LessThanEqualTo:
                comp = "≤"
            case types.GreaterThanEqualTo:
                comp = "≥"

        return f"If {block.head.left.value}{comp}{block.head.right.value}\nThen\n{"\n".join([create_command(comm) for comm in block.body])}\nEnd"
    elif issubclass(type(block), types.While):
        comp = ""
        match type(block.head):
            case types.LessThan:
                comp = "<"
            case types.GreaterThan:
                comp = ">"
            case types.EqualTo:
                comp = "="
            case types.NotEqualTo:
                comp = "≠"
            case types.LessThanEqualTo:
                comp = "≤"
            case types.GreaterThanEqualTo:
                comp = "≥"
        return f"While {block.head.left.value}{comp}{block.head.right.value}\n{"".join([create_command(comm) for comm in block.body])}End"

def create_command(command: types.Assign | types.Call | types.Block):
    if type(command) == types.Assign:
        return assign_val(command) + "\n"
    elif type(command) == types.Call:
        return call_func(command) + "\n"
    elif issubclass(type(command), types.Block):
        return create_block(command) + "\n"
    
    return "\n"