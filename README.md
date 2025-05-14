# TI-Python
A versatile compiler to make TI-BASIC programs from Python 3 (with some restrictions)

## Installation
```
pip install ti-python
```
Note that the PyPi package is probably severely out of date and is updated very irregularly

## Usage
### CLI
```
python -m ti_python --help
```
or
```
ti-python --help
```

<br>

### Compiling
```
python -m ti_python examples/helloworld.py
```
```py
from ti_python import compile
code = "print('Hello World!')"
print(compile(code))
```

See `examples/` for example programs

### Decompiling 8XP
`ti-python` comes with a 8XP decompiler to get the TI-BASIC source from an 8XP file

```
python -m ti_python --decompile myprogram.8xp
```

## Features
 - `print` and `input`
 - Integer and string variables (with multi-character names)
 - Basic arithmetic
 - Basic If statements
 - Comparisons
 - While loops
 - String operations
 - Pixel graphics functions (use `clear_screen()` and `pixel_on/off(y,x,COLOR_NAME)`)
 - Lists
 - 8XP Decompiler

## Goals/To Do
 - Functions
 - Advanced/Polished graphical output
 - More advanced comparisons and operations (exponents, roots, `and`, `or`)

Non-compiler related
 - 8XP compiler

## Restrictions
Your Python code still has to follow some restrictions due to the nature of the TI-BASIC.
 - Using `print` with commas will not insert spaces in-between 
 - The `input` function doesn't always return Strings, they can be numbers
 - Lists are 1-indexed

These are known restrictions, but this compiler is still in development so of course you will still have *many* other issues

## Resources and References Used
[TI-BASIC usage](http://tibasicdev.wikidot.com/starter-kit)
[More TI-BASIC Docs](https://learn.cemetech.net/)
[8XP File Format](https://gist.github.com/SimonEast/244a0fd04526ea1acbec2e2ceb2e7924)