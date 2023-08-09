#!/usr/bin/env python3
"""
measure_runtime should measure the total runtime and return it
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime should measure the total runtime and return it"""
    time_start = time.perf_counter()
    task = [async_comprehension() for i in range(4)]
    await asyncio.gather(*task)
    time_end = time.perf_counter()
    return (time_end - time_start)
