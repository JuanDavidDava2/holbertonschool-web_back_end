#!/usr/bin/env python3
"""Async Generator"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """each time asynchronously wait 1 second, then yield a
    random number between 0 and 10. Use the random module."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
