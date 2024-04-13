from datetime import time
from itertools import permutations


async def solution(a: int, b: int, c: int, d: int) -> list[time]:
    """Return all the possible valid times from the given numbers"""
    possible_times = set(permutations((a, b, c, d)))
    valid_time = []

    for value in possible_times:
        hours = int("".join(str(ch) for ch in value[:2]))
        minutes = int("".join(str(ch) for ch in value[2:]))
        try:
            clock = time(hours, minutes)
        except ValueError:
            continue

        valid_time.append(clock)

    valid_time.sort()
    return valid_time
