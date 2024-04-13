import pytest

from lesson3.tape_equilibrium import solution


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([3, 1, 2, 4, 3], 1),
        ([-1000, 1000], 2000),
    ],
)
@pytest.mark.asyncio
async def test_solution(numbers: list[int], expected: int) -> None:
    """Test tape equilibrium solution"""
    assert await solution(numbers) == expected
