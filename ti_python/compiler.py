"""
Core converter from Python to a TI-BASIC representation to be used in the `generate` module
"""

import ast

from . import generate, types

builtins = {
    "print": "Disp ",
    "input": "Input ",
    "clear_screen": "ClrDraw",
    "pixel_on": "Pxl-On(",
    "pixel_off": "Pxl-Off(",
    "draw_line": "Line(",

    "cos": "cos(",
    "sin": "sin(",
    "tan": "tan(",
    "acos": "acos(",
    "asin": "asin(",
    "atan": "atan(",
    "sqrt": "√(",
    "abs": "abs(",
    "round": "round(",
    "int": "int(",
    "rand": "rand(",
    "randint": "randInt(",
    "randrange": "randInt(",
    "len": "dim(",
}  # Not common, but there may be functions that can be mapped directly to TI-BASIC functions

keywords = [
    "BLUE",
    "RED",
    "BLACK",
    "MAGENTA",
    "GREEN",
    "ORANGE",
    "BROWN",
    "NAVY",
    "LTBLUE",
    "YELLOW",
    "WHITE",
    "LTGRAY",
    "MEDGRAY",
    "GRAY",
    "DARKGRAY",
]

variable_map = {}  # All new variable names will be mapped to characters here
name_map = "ABCDEFGHIJKLMNOPQRSTUVWXYZθ"  # A-Z + Theta


def flatten_value(
    value: ast.Constant | ast.Name | ast.Call | ast.BinOp,
) -> types.Type | types.Call | types.Assign:
    "Converts any constant, variable, or expression (and their children) into a single `Type` object"
    if type(value) == ast.Constant:
        return (
            types.Str(value.value)
            if type(value.value) == str
            else types.Number(value.value)
        )

    elif type(value) == ast.Name:
        if value.id.upper() in keywords:
            return types.Name(value.id.upper())

        if value.id.upper() not in variable_map:
            variable_map[value.id.upper()] = name_map[len(variable_map)]

        return types.Name(variable_map[value.id.upper()])

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

    elif type(value) == ast.Compare:
        if type(value.ops[0]) == ast.Lt:
            return types.LessThan(
                flatten_value(value.left), flatten_value(value.comparators[0])
            )
        if type(value.ops[0]) == ast.Gt:
            return types.GreaterThan(
                flatten_value(value.left), flatten_value(value.comparators[0])
            )
        if type(value.ops[0]) == ast.LtE:
            return types.LessThanEqualTo(
                flatten_value(value.left), flatten_value(value.comparators[0])
            )
        if type(value.ops[0]) == ast.GtE:
            return types.GreaterThanEqualTo(
                flatten_value(value.left), flatten_value(value.comparators[0])
            )
        if type(value.ops[0]) == ast.Eq:
            return types.EqualTo(
                flatten_value(value.left), flatten_value(value.comparators[0])
            )
        if type(value.ops[0]) == ast.NotEq:
            return types.NotEqualTo(
                flatten_value(value.left), flatten_value(value.comparators[0])
            )

    elif type(value) == ast.List:
        return types.List([flatten_value(v) for v in value.elts])

    elif type(value) == ast.Subscript:
        return types.Slice(flatten_value(value.slice), flatten_value(value.value))


def flatten_command(command: ast.AST):
    "This to to convert non-value items into an object (eg. Assigment, Loop, etc)"
    if type(command) == ast.Assign:
        # No support for multiple targets or values. Single target and value only.
        target = flatten_value(command.targets[0])
        var_value = flatten_value(command.value)

        if type(var_value) == types.Call and var_value.value == "Input ":
            return types.Call("Input ", var_value.args + [target])
        return types.Assign(target, var_value)

    elif type(command) == ast.Expr:
        return flatten_value(command.value)

    elif type(command) == ast.Call:
        return flatten_value(command)

    elif type(command) == ast.If:
        comparison = flatten_value(command.test)

        body = [flatten_command(comm) for comm in command.body]

        return types.If(comparison, body)

    elif type(command) == ast.While:
        comparison = flatten_value(command.test)

        body = [flatten_command(comm) for comm in command.body]

        return types.While(comparison, body)


def compile_tree(tree: ast.Module):
    compiled = ""
    for item in tree.body:
        command = flatten_command(item)
        compiled += generate.create_command(command)
    return compiled
