"""
Generates TI-BASIC commands from parameters
"""
from . import types

    

def call_func(call: types.Call):
    arguments = []

    if call.args:
        for arg in call.args:
            if type(arg) == types.Str:
                arguments.append(f'"{arg.value}"')
            elif type(arg) == types.Number:
                arguments.append(str(arg.value))
            elif type(arg) == types.Name:
                arguments.append(arg.value.upper())
    return f"{call.value} {','.join(arguments)}"

def assign_val(assign: types.Assign):
    if type(assign.value) == types.Number:
        return f"{assign.value.value}->{assign.target.value.upper()}"
    elif type(assign.value) == types.Call:
        return f"{call_func(assign.value)}->{assign.target.value.upper()}"
    elif issubclass(type(assign.value), types.Op):
        match type(assign.value):
            case types.Add:
                op = "+"
            case types.Sub:
                op = "-"
            case types.Mul:
                op = "*"
            case types.Div:
                op = "/"
        return f"{assign.value.left.value}{op}{assign.value.right.value}->{assign.target.value.upper()}"