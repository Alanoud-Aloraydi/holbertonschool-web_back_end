# Python Async Comprehension

This project explores asynchronous generators and comprehensions in Python. It builds on `asyncio` by producing values over time, collecting them with concise async comprehension syntax, and running several comprehensions concurrently.

## Learning Objectives

By completing this project, you should be able to explain:

- how to write an asynchronous generator;
- how `yield` works inside an `async def` function;
- how to consume values with `async for`;
- how to write an asynchronous comprehension;
- how to annotate an asynchronous generator;
- how `asyncio.gather()` runs awaitable operations concurrently.

## Core Concepts

An asynchronous generator can pause with `await` and produce several values with `yield`. Its caller consumes those values using `async for`. The return annotation `AsyncGenerator[float, None]` states that the generator yields floats and does not accept values through `asend()`.

An async comprehension uses the same idea in a compact expression:

```python
values = [value async for value in async_generator()]
```

Four comprehensions still take roughly ten seconds when they run through `asyncio.gather()`. Each comprehension performs ten one-second waits, but the four independent waits overlap instead of running one comprehension after another.

## Files

| File | Description |
| --- | --- |
| `0-async_generator.py` | Yields ten random floats with asynchronous delays. |
| `1-async_comprehension.py` | Collects generator values with an async comprehension. |
| `2-measure_runtime.py` | Measures four comprehensions running concurrently. |

## Style Check

```bash
pycodestyle --version
pycodestyle *.py
```
