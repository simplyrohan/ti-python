import ast


def print_tree(node):
    match type(node):
        case ast.Module:
            for n in node.body:
                print_tree(n)
        case ast.Expr:
            print_tree(node.value)
        case ast.Call:
            print(
                f"{node.func.id}({', '.join([str(arg.value) for arg in node.args])})"
            )


def parse(code):
    parsed = ast.parse(code)

    # print_tree(parsed)

    return ast.parse(code)
