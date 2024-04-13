import pytest

from lesson1.binary_gap import solution


@pytest.mark.parametrize(
    "number, expected",
    [
        (9, 2),
        (529, 4),
        (20, 1),
        (15, 0),
        (32, 0),
        (1041, 5),
        (2147483647, 0),
    ],
)
@pytest.mark.asyncio
async def test_solution(number: int, expected: int) -> None:
    """Test binary gap solution"""
    assert await solution(number) == expected
