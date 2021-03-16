#!/usr/bin/env python3
"""
    at the same time with async
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """execute n times wait_random method"""
    list_of_delays: List[float] = []
    for _ in range(n):
        list_of_delays.append(await wait_random(max_delay))
    return sorted(list_of_delays)