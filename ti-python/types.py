from __future__ import annotations
import dataclasses


# ---- Types
@dataclasses.dataclass
class Type:
    value: str


class Number(Type):
    pass


class Str(Type):
    pass


class Var(Type):
    pass


class Name(Type):
    pass


# --- Calls, Assigns, and Control Flow
@dataclasses.dataclass
class Call:
    value: str
    args: list[Type]


@dataclasses.dataclass
class Assign:
    target: Type
    value: Type


@dataclasses.dataclass
class Block:
    head: Op | Type
    body: list


class If(Block):
    pass

class While(Block):
    pass

# ---- Operations
@dataclasses.dataclass
class Op:
    left: Type
    right: Type


class Add(Op):
    pass


class Sub(Op):
    pass


class Mul(Op):
    pass


class Div(Op):
    pass


class Comp(Op):
    pass


class LessThan(Comp):
    pass


class GreaterThan(Comp):
    pass
