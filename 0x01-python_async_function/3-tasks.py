#!/usr/bin/env python3
"""
This module is a regular function that takes an integer
max_delay and returns a asyncio.task
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    This function returns an asyncio.Task
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
