import pytest

from lesson4.missing_integer import solution


@pytest.mark.parametrize("arr, expected", [([1, 3, 6, 4, 1, 2], 5), ([1, 2, 3], 4), ([-1, -3], 1)])
@pytest.mark.asyncio
async def test_missing_integer_is_working(arr: list[int], expected: int) -> None:
    """Test that the function returns the smallest positive integer that does not occur in a given sequence."""
    assert await solution(arr) == expected
