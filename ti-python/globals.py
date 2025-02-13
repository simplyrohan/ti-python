import dataclasses

@dataclasses.dataclass
class Type:
    value: str

class Number(Type): pass

class Str(Type): pass

class Var(Type): pass