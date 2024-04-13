async def solution(arr: list) -> int:
    """Returns 1 if the array is a permutation and 0 if it is not."""
    max_value = max(arr)
    return 1 if len(arr) == len(set(arr)) and sum(set(arr)) - (max_value * (max_value + 1) // 2) == 0 else 0
