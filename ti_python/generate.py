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
        return f'"{val.value}"'
    elif issubclass(type(val), types.Op):
        if type(val) == types.Add:
            op = "+"
        elif type(val) == types.Sub:
            op = "-"
        elif type(val) == types.Mul:
            op = "*"
        elif type(val) == types.Div:
            op = "/"
        return f"{create_val(val.left)}{op}{create_val(val.right)}"
    elif type(val) == types.List:
        return "{" + ",".join(create_val(v) for v in val.value) + "}"

def call_func(call: types.Call):
    arguments = []

    if call.args:
        for arg in call.args:
            arguments.append(create_val(arg))
    return f"{call.value}{','.join(arguments)}"


def assign_val(assign: types.Assign):
    if type(assign.value) == types.List:
        return create_val(assign.value) + f"→∟{assign.target.value.upper()}"
            
    return create_val(assign.value) + f"→{assign.target.value.upper()}"


def create_block(block: types.Block):
    if issubclass(type(block), types.If) or issubclass(type(block), types.While):
        comp = ""
        if type(block.head) == types.LessThan:
            comp = "<"
        elif type(block.head) == types.GreaterThan:
            comp = ">"
        elif type(block.head) == types.EqualTo:
            comp = "="
        elif type(block.head) == types.NotEqualTo:
            comp = "≠"
        elif type(block.head) == types.LessThanEqualTo:
            comp = "≤"
        elif type(block.head) == types.GreaterThanEqualTo:
            comp = "≥"

        if issubclass(type(block), types.If):
            nl = "\n"
            return f"If {block.head.left.value}{comp}{block.head.right.value}\nThen\n{nl.join([create_command(comm) for comm in block.body])}\nEnd"
        else:
            return f"While {block.head.left.value}{comp}{block.head.right.value}\n{''.join([create_command(comm) for comm in block.body])}End"


def create_command(command: types.Assign | types.Call | types.Block):
    if type(command) == types.Assign:
        return assign_val(command) + "\n"
    elif type(command) == types.Call:
        return call_func(command) + "\n"
    elif issubclass(type(command), types.Block):
        return create_block(command) + "\n"

    return "\n"
