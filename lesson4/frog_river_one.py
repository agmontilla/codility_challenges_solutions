async def solution(position_x: int, falling_leaves: list[int]) -> int:
    """Returns the earliest time when the frog can jump to the other side of the river."""
    leaves = {}

    if sum(set(falling_leaves)) - (position_x * (position_x + 1) // 2) != 0:
        return -1

    for second, position in enumerate(falling_leaves):
        if position not in leaves:
            leaves[position] = second

    return max(leaves.values())
