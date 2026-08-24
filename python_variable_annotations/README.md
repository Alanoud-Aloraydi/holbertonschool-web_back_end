# Python Variable Annotations

This project introduces type annotations in Python 3. Type annotations describe the expected types of function parameters, return values, and variables. They make code easier to understand and allow static type checkers to detect mistakes before the program runs.

## Learning Objectives

By completing this project, you should be able to explain:

- how to annotate function parameters and return values;
- how to annotate variables;
- how to describe lists, tuples, mappings, unions, optional values, and callable objects;
- how duck typing focuses on an object's supported behavior instead of its exact class;
- how to use `mypy` to validate annotated Python code.

## Type Annotations

A function signature can state the types it expects and returns:

```python
def add(a: float, b: float) -> float:
    return a + b
```

Annotations do not enforce types while Python is running. They provide useful information to readers, editors, and static analysis tools such as `mypy`.

## Duck Typing

Duck typing describes an object by the operations it supports. For example, a function that only needs to iterate over its input can accept an `Iterable` rather than requiring a specific type such as `list`. This makes the function more flexible while its annotation still explains what behavior is required.

## Files

| File | Description |
| --- | --- |
| `0-add.py` | Adds two floating-point numbers. |
| `1-concat.py` | Concatenates two strings. |
| `2-floor.py` | Returns the floor of a float. |
| `3-to_str.py` | Converts a float to a string. |
| `4-define_variables.py` | Defines annotated variables. |
| `5-sum_list.py` | Sums a list of floats. |
| `6-sum_mixed_list.py` | Sums integers and floats. |
| `7-to_kv.py` | Returns a key and a squared numeric value. |
| `8-make_multiplier.py` | Creates a multiplier function. |
| `9-element_length.py` | Uses duck typing with iterable sequences. |
| `100-safe_first_element.py` | Safely returns the first sequence element. |
| `101-safely_get_value.py` | Retrieves a mapping value with a typed default. |
| `102-type_checking.py` | Contains code corrected and validated with `mypy`. |

## Validation

Run the following commands from the project directory:

```bash
pycodestyle --version
pycodestyle *.py
mypy 102-type_checking.py
```
