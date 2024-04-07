async def solution(numbers: list[int]) -> int:
    """Returns the missing element in the list"""
    maximum_element = len(numbers) + 1

    gauss_sum = int(maximum_element * (maximum_element + 1) / 2)

    return gauss_sum - sum(numbers)
