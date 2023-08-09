#!/usr/bin/env python3
"""
Measures the total execution time for wait_n function and
returns total_time/n.
"""
import time
import asyncio
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


# Define the measure_time function
def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n function and
    returns total_time/n.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
