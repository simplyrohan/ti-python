import ast

from . import generate
from .globals import *

builtins = {"print": "Disp"}

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

        if function_name in builtins:
            return generate.call_func(builtins[function_name], function_args)
        else:
            return generate.call_func(function_name, function_args)

def compile(tree: ast.Module):
    compiled = ""
    for item in tree.body:
        print(item)
        if type(item) == ast.Expr:
            compiled += flatten_expression(item) + "\n"
    
    return compiled
