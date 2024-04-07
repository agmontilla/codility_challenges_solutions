from collections import Counter


async def solution(sample: list) -> int:
    """Returns the unpaired element in the list"""
    stats = Counter(sample)

    unpaired_element = 0

    for k, v in stats.items():
        if v % 2 != 0:
            unpaired_element = k
            break

    return unpaired_element
