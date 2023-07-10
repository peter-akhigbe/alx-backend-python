#!/usr/bin/env python3
'''defines wait_random function'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    Args:
        max_delay : int
    returns:
        random float
    '''
    rand_delay = random.uniform(0, max_delay)
    await asyncio.sleep(rand_delay)
    return rand_delay

asyncio.run(wait_random())
