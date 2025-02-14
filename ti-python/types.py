import dataclasses

# ---- Types
@dataclasses.dataclass
class Type:
    value: str

class Number(Type): pass

class Str(Type): pass

class Var(Type): pass

class Name(Type): pass

# --- Calls and Assigns
@dataclasses.dataclass
class Call:
    value: str
    args: list[Type]

@dataclasses.dataclass
class Assign:
    target: Type
    value: Type

# ---- Operations
@dataclasses.dataclass
class Op:
    left: Type
    right: Type

class Add(Op): pass
class Sub(Op): pass
class Mul(Op): pass
class Div(Op): pass

