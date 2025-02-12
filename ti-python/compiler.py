import ast

from . import generate

builtins = {"print": "Disp"}


def flatten_expression(expression: ast.Expr):
    if type(expression.value) == ast.Call:
        function_name = expression.value.func.id

        function_args = [arg.value for arg in expression.value.args]

        if function_name in builtins:
            return generate.call_func(builtins[function_name], function_args)
        else:
            return generate.call_func(function_name, function_args)

def compile(tree: ast.Module):
    compiled = ""
    for item in tree.body:
        if type(item) == ast.Expr:
            compiled += flatten_expression(item) + "\n"
    
    return compiled
