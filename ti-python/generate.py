"""
Creates TI-BASIC commands through functions
"""

def call_func(name: str, args: list = None):
    arguments = []

    if args:
        for arg in args:
            if type(arg) == str:
                arguments.append(f'"{arg}"')
    return f":{name} {" ".join(arguments)}"
