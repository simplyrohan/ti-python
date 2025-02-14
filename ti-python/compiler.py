"""
Core converter from Python to TI-BASIC commands
"""

import ast

from . import generate
from .globals import *

builtins = {
    "print": "Disp",
    "input": "Input",
}  # Not common, but there may be functions that can be mapped directly to TI-BASIC functions

variables = {}


def get_name(node: ast.Name | ast.Constant):
    if type(node) == ast.Name:
        return Var(node.id)
    elif type(node) == ast.Constant:
        if type(node.value) == str:
            return Str(node.value)
        elif type(node.value) == int:
            return Number(node.value)


def flatten_expression(expression: ast.Expr):
    if type(expression.value) == ast.Call:
        function_name = expression.value.func.id

        function_args = [get_name(arg) for arg in expression.value.args]

        # if function_name in builtins:
        #     return generate.call_func(builtins[function_name], function_args)
        # else:
        #     return generate.call_func(function_name, function_args)

        if function_name in builtins:
            return builtins[function_name], function_args
        else:
            return function_name, function_args


def flatten_op(op: ast.BinOp):
    print(get_name(op.left), get_name(op.right), op.op)
    match type(op.op):
        case ast.Add:
            return f"{get_name(op.left).value} + {get_name(op.right).value}"


def flatten_assign(assign: ast.Assign):
    # No support for multiple targets or values. Single target and value only.

    target = get_name(assign.targets[0])
    match type(assign.value):
        case ast.Name | ast.Constant:
            value = get_name(assign.value)
        case ast.Call:
            value = flatten_expression(assign)
            if value[0] == "Input":
                return generate.call_func("Input", value[1] + [target])
        case ast.BinOp:
            value = Var(flatten_op(assign.value))
    return generate.store_var(target, value)


def compile(tree: ast.Module):
    compiled = ""
    for item in tree.body:
        if type(item) == ast.Expr:
            compiled += generate.call_func(*flatten_expression(item)) + "\n"

        if type(item) == ast.Assign:
            compiled += flatten_assign(item) + "\n"

    return compiled
