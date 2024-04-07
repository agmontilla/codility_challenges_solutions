async def solution(number: int) -> int:
    """Returns the binary gap of a number"""
    binary = bin(number)[2:]
    max_gap = 0
    gap = 0
    for digit in binary:
        if digit == "0":
            gap += 1
            continue

        max_gap = max(max_gap, gap)
        gap = 0

    return max_gap
