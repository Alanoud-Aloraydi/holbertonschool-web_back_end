# Python Async Function

This project introduces asynchronous programming in Python with `asyncio`. It demonstrates how coroutines can pause while waiting, how several coroutines can run concurrently, and how tasks schedule coroutine execution on an event loop.

## Learning Objectives

By completing this project, you should be able to explain:

- how to define coroutines with `async def`;
- how `await` pauses one coroutine without blocking the event loop;
- how to run an asynchronous program with `asyncio.run()`;
- how to execute multiple coroutines concurrently;
- how to create and use `asyncio.Task` objects;
- how to generate floating-point values with `random.uniform()`.

## Core Concepts

A coroutine is a function whose execution can be suspended and resumed. When a coroutine awaits an operation such as `asyncio.sleep()`, the event loop can run other ready work instead of waiting idly. This concurrency is useful for programs that spend time waiting for timers, network responses, files, or other input and output operations.

An `asyncio.Task` wraps a coroutine and schedules it to run on the active event loop. `asyncio.as_completed()` can then yield concurrent operations in the order they finish.

## Files

| File | Description |
| --- | --- |
| `0-basic_async_syntax.py` | Waits for and returns a random delay. |
| `1-concurrent_coroutines.py` | Runs several random-delay coroutines concurrently. |
| `2-measure_runtime.py` | Measures the average runtime per coroutine. |
| `3-tasks.py` | Creates an `asyncio.Task` for a random delay. |
| `4-tasks.py` | Runs multiple task-based delays concurrently. |

## Example

```python
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random
print(asyncio.run(wait_random(1)))
```

The printed value is a random float between `0` and `1`, and the coroutine waits for approximately that many seconds before returning it.

## Style Check

```bash
pycodestyle --version
pycodestyle *.py
```
