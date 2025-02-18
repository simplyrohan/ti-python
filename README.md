# TI-Python
A versatile compiler to make TI-BASIC programs from Python 3 (with some restrictions)

## Usage
**CLI**
```
python -m ti_python --help
```
```
python -m ti_python examples/helloworld.py
```

**Python**
```py
from ti_python import compile
code = "print('Hello World!')"
print(compile(code))
```

See `examples/` for example programs

## Features
 - `print` and `input`
 - Integer variables
 - Basic arithmetic
 - Basic If statements
 - Comparisons
 - While loops
 - Strings and string operations

## Goals/To Do
 - Lists
 - Functions
 - Graphical output
 - Variable mapping (allows for longer variable names)
 - More advanced comparisons and operations (exponents, roots, `and`, `or`)

Non-compiler related
 - 8XP encoding
 - Web TI-Basic interpreter

## Restrictions
Your Python code still has to follow some restrictions due to the nature of the TI-BASIC.
 - One letter variables names (this may be fixed soon) 
 - Using `print` with commas will not insert spaces in-between 
 - The `input` function doesn't always return Strings, they can be numbers

These are known and intentional restrictions, but this compiler is still in development so of course you will still have *many* problems

## Resources and References Used
[TI-BASIC usage](http://tibasicdev.wikidot.com/starter-kit)
