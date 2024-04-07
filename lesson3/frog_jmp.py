from math import ceil


async def solution(x: int, y: int, d: int) -> int:
    """Returns the minimal number of jumps from position x to y"""
    return ceil((y - x) / d)
