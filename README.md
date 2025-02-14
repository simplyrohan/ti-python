# TI-Python
A versatile compiler to make TI-BASIC programs from Python 3 (with some restrictions)

## Usage
```
python -m ti-python --help
```
```
python -m ti-python examples/helloworld.py
```

See `examples/` for example programs

## Features
 - `print` and `input`
 - Integer variables
 - Basic arithmetic

## Restrictions
Your Python code still has to follow some restrictions due to the nature of the TI-BASIC.
 - One letter variables names (this may be fixed soon) 
 - Using `print` with commas will not insert spaces in-between 
These are known and intentional restrictions, but this compiler is still in development so of course you will still have *many* problems

## Resources and References Used
[TI-BASIC usage](http://tibasicdev.wikidot.com/starter-kit)
