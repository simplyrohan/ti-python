"""
Core converter from Python to a TI-BASIC representation to be used in the `generate` module
"""

import ast

from . import generate, types

builtins = {
    "print": "Disp",
    "input": "Input",
}  # Not common, but there may be functions that can be mapped directly to TI-BASIC functions


def flatten_value(value: ast.Constant | ast.Name | ast.Call | ast.BinOp) -> types.Type | types.Call | types.Assign:
    "Converts any constant, variable, or expression (and their children) into a single `Type` object"

    if type(value) == ast.Constant:
        return types.Str(value.value) if type(value.value) == str else types.Number(value.value)

    elif type(value) == ast.Name:
        return types.Name(value.id.upper())

    elif type(value) == ast.Expr:
        return flatten_value(value.value)

    elif type(value) == ast.Call:
        func = (
            value.func.id if value.func.id not in builtins else builtins[value.func.id]
        )
        args = [flatten_value(arg) for arg in value.args]
        return types.Call(func, args)

    elif type(value) == ast.BinOp:
        if type(value.op) == ast.Add:
            return types.Add(flatten_value(value.left), flatten_value(value.right))
        elif type(value.op) == ast.Sub:
            return types.Sub(flatten_value(value.left), flatten_value(value.right))
        elif type(value.op) == ast.Mult:
            return types.Mul(flatten_value(value.left), flatten_value(value.right))
        elif type(value.op) == ast.Div:
            return types.Div(flatten_value(value.left), flatten_value(value.right))

def flatten_command(command: ast.AST):
    "This to to convert non-value items into an object (eg. Assigment, Loop, etc)"
    if type(command) == ast.Assign:
        # No support for multiple targets or values. Single target and value only.
        target = flatten_value(command.targets[0])
        var_value = flatten_value(command.value)

        if type(command) == types.Call and var_value.value == "Input":
            return types.Call("Input", var_value.args + [target])
        return types.Assign(target, var_value)

    elif type(command) == ast.Expr:
        return flatten_value(command.value)

    elif type(command) == ast.Call:
        return flatten_value(command)

def compile(tree: ast.Module):
    compiled = ""
    for item in tree.body:
        command = flatten_command(item)

        if type(command) == types.Assign:
            compiled += generate.assign_val(command) + "\n"
        elif type(command) == types.Call:
            compiled += generate.call_func(command) + "\n"

    return compiled
